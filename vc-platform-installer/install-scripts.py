import sys
import datetime
import os
import urllib.request 
import glob
import shutil

script_url = sys.argv[1]
destination_folder = sys.argv[2]
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
    os.remove('script.zip')

if(os.path.exists(destination_folder)):
    download_script()
else:
    print('Destinantion folder not exists') 