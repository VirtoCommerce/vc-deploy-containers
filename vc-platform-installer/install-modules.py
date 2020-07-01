#!/usr/bin/python
import zipfile 
import io 
import urllib.request
import json
import zipfile
import shutil
import sys

def getZipData(url):
    result = urllib.request.urlopen(url)
    return result.read()

platformConfigUri = sys.argv[1]
modulesFolder = sys.argv[2]

print("Downloading from", platformConfigUri)
print("Destination folder", modulesFolder)

with urllib.request.urlopen(platformConfigUri) as response, open('platform.json', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

with open('platform.json') as f:
    config = json.load(f)
    for module in config["Modules"]:
        moduleId = module["Id"]
        packageUrl = module["PackageUrl"]
        destinationPath = modulesFolder + moduleId
        zipData = getZipData(packageUrl)
        zipRef = zipfile.ZipFile(io.BytesIO(zipData))
        zipRef.extractall(destinationPath)
        print(moduleId, 'installed')