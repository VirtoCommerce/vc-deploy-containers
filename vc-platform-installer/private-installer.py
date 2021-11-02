import sys
import datetime
import os
import requests
import shutil
import json
from zipfile import ZipFile

inputjson = sys.argv[1]
api_token = os.environ.get('AUTH_TOKEN')

get_headers = headers = {
    'Authorization': f'token {api_token}',
    'Accept': 'application/vnd.github.v3+json'
}

download_headers = headers = {
    'Authorization': f'token {api_token}',
    'Accept': 'application/octet-stream'
}


def log(message):
    time = datetime.datetime.now()
    print('{}: {}'.format(time, message))


def removing_old_source(path):
    log('Removing old source...')
    for the_file in os.listdir(path):
        file_path = os.path.join(path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    log('Removing complete')


def main():
    data = json.loads(inputjson)
    for target in data:
        repository = target.get('Repository')
        tag = target.get('Tag')
        destination = target.get('Destination')
        source_type = target.get('Type')
        get_url = f'https://api.github.com/repos/{repository}/releases/tags/{tag}'
        release = requests.get(get_url, headers=get_headers)
        log('{}'.format('Downloading... '))
        download = requests.get(release.json()['assets'][0]['url'], headers=download_headers, stream=True)
        if not os.path.exists(destination): os.makedirs(destination)
        removing_old_source(destination)
        if download.status_code == 200:
            with open('tmp.zip', 'wb') as f:
                download.raw.decode_content = True
                shutil.copyfileobj(download.raw, f)
        log('{}'.format('Installing... '))
        with ZipFile('tmp.zip', 'r') as zipObject:
            listOfFileNames = zipObject.namelist()
            for fileName in listOfFileNames:
                    zipObject.extract(fileName, destination)
                    log('{}{}'.format('Extraction...', fileName))
        log('{}'.format('Installing complete! '))
        os.unlink('tmp.zip')


if __name__ == '__main__':
    main()