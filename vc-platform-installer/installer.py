import sys
import datetime
import os
import urllib.request 
import zipfile 
import shutil

from zipfile import ZipFile

def log(message):
    time = datetime.datetime.now()
    print('{}: {}'.format(time, message))

def unique_archive_name():
    exec_time = str(datetime.datetime.now())
    return print('{}.zip'.format(exec_time[-6:-1]))

def install():  
    log('{}{}'.format('Downloading zip from:', inputzipfile))
    url = inputzipfile
    zip_name = '\"unique_archive_name()\"'
    urllib.request.urlretrieve(url, zip_name)
    log('Zip successfuly downloaded!')
    with ZipFile(zip_name, 'r') as zipObject:
        listOfFileNames = zipObject.namelist()
        for fileName in listOfFileNames:
                zipObject.extract(fileName, destination_folder)
                log('{}{}'.format('Extraction...', fileName))
    installed_assets = open(installed_source, 'w')
    installed_assets.write(inputzipfile)
    installed_assets.close()
    os.remove(zip_name)

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

### BEGIN

inputzipfile = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder): os.mkdir(destination_folder)
installed_source = os.path.join(destination_folder, 'installed_source.txt')

if(os.path.exists(installed_source)):
    check_assets_version = open(installed_source, 'r')
    current_version = check_assets_version.read()
    check_assets_version.close()
    if current_version != inputzipfile:
        removing_old_source(destination_folder)
        install() 
    else:
        log('Destination folder up to date')
else:
    removing_old_source(destination_folder)
    install()
### END