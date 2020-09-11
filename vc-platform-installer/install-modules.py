#!/usr/bin/python
import zipfile 
import io 
import urllib.request
import json
import zipfile
import os
import shutil
import sys
import datetime
print('START:'); print(datetime.datetime.now())
def getZipData(url):
    result = urllib.request.urlopen(url)
    return result.read()

platformConfigUri = sys.argv[1]
modulesFolder = sys.argv[2]

print("Clearing up the destination folder", modulesFolder)
for filename in os.listdir(modulesFolder):
    file_path = os.path.join(modulesFolder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

print("Downloading from", platformConfigUri)
print("Destination folder", modulesFolder)
print('DELETE_COMPLETE:'); print(datetime.datetime.now())
with urllib.request.urlopen(platformConfigUri) as response, open('modules.json', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

with open('modules.json') as f:
    config = json.load(f)
    for module in config:
        moduleId = module["Id"]
        packageUrl = module["PackageUrl"]
        print('downloading', packageUrl)        
        destinationPath = modulesFolder + moduleId
        zipData = getZipData(packageUrl)
        zipRef = zipfile.ZipFile(io.BytesIO(zipData))
        zipRef.extractall(destinationPath)
        print(moduleId, 'installed')
print('INSTALL_COMPLETE:'); print(datetime.datetime.now())