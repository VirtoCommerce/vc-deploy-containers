import sys
import datetime
import os
import urllib.request 
import zipfile 
import shutil

inputzipfile = sys.argv[1]
assetsFolder = sys.argv[2]
checkFolder = os.path.join(assetsFolder, 'assets')
installed_assets_file = os.path.join(checkFolder, 'installed_assets.txt')

from zipfile import ZipFile
def download_assets():
    print(datetime.datetime.now())
    print('Downloading assets from:', inputzipfile)
    url = inputzipfile
    urllib.request.urlretrieve(url, "assets.zip")
    print(datetime.datetime.now())
    print('Assets successfuly downloaded!')
    with ZipFile('assets.zip', 'r') as zipObject:
        listOfFileNames = zipObject.namelist()
        for fileName in listOfFileNames:
                zipObject.extract(fileName, assetsFolder)
                print('Extraction...', fileName) 
    installed_assets = open(installed_assets_file, 'w')
    text_for_file = inputzipfile
    installed_assets.write(text_for_file)
    os.remove('assets.zip')

def removing_old_assets(path):
    if(os.path.exists(checkFolder)):
        print(datetime.datetime.now())
        print('Removing old assets...')
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

if(os.path.exists(installed_assets_file)):
    check_assets_version = open(installed_assets_file, 'r')
    current_version = check_assets_version.read()
    if current_version != inputzipfile:
        removing_old_assets(checkFolder)
        download_assets() 
    else:
        print('Assets up to date')
else:
    removing_old_assets(checkFolder)
    download_assets()

