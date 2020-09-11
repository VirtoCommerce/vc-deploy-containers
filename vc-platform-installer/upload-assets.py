import sys
import datetime
import os
import urllib.request 
import tqdm
import zipfile 

inputzipfile = sys.argv[1]
assetsFolder = sys.argv[2]
checkFolder = (assetsFolder + '/assets')
from zipfile import ZipFile
from tqdm import tqdm
if(os.path.exists(checkFolder)):
    print('Assets already exists')
else:
    print('Downloading assets...'); print(datetime.datetime.now())
    url = inputzipfile
    urllib.request.urlretrieve(url, "assets.zip")
    print('Downloading assets successfuly !'); print(datetime.datetime.now()) 
    print('Starting unarchiving!')
    with ZipFile(file='assets.zip') as zip_file:
        for file in tqdm(iterable=zip_file.namelist(), total=len(zip_file.namelist())):
            zip_file.extract(member=file, path=assetsFolder)
    print('Unarchiving successfuly !'); print(datetime.datetime.now())  

