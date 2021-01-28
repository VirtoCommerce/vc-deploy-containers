import sys
import datetime
import os
import urllib.request 
import glob
import shutil

script_url = sys.argv[1]
destination_folder = sys.argv[2]
installed_script_file = os.path.join(destination_folder, 'installed_scripts.txt')
from zipfile import ZipFile

def download_script():
    print(datetime.datetime.now())
    print('Downloading script from:', script_url)
    url = script_url
    urllib.request.urlretrieve(url, "script.zip")
    print(datetime.datetime.now())
    print('Script successfuly downloaded!')
    with ZipFile('script.zip', 'r') as zipObject:
        listOfFileNames = zipObject.namelist()
        for fileName in listOfFileNames:
                zipObject.extract(fileName, destination_folder)
                print('Extraction...', fileName)
    installed_script = open(installed_script_file, 'w')
    text_for_file = script_url
    installed_script.write(text_for_file) 
    os.remove('script.zip')

def removing_old_script(path):
    print(datetime.datetime.now())
    print('Removing old script...')
    folder = path
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    print(datetime.datetime.now())
    print('Removing complete') 

if(os.path.exists(installed_script_file)):
    check_theme_version = open(installed_script_file, 'r')
    current_version = check_theme_version.read()
    if current_version != script_url:
        removing_old_script(destination_folder)
        download_script() 
    else:
        print('Theme up to date')
else:
    removing_old_script(destination_folder)
    download_script() 