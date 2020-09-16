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
import threading

### Declarations
class Module:
    def __init__(self, id, url, version):
        self.id = id
        self.url = url
        self.version = version

def getZipData(url):
    result = urllib.request.urlopen(url)
    return result.read()

def getModuleVersion(versions):
    for version in versions:
        if not version["VersionTag"]:
            return version["Version"]

def getModuleUrl(versions):
    for version in versions:
        if not version["VersionTag"]:
            return version["PackageUrl"]

def installModule(module: Module, modulesFodler: str):
    log(f"Install module: {module.id}")
    destinationPath = os.path.join(modulesFolder, module.id)
    zipData = getZipData(module.url)
    zipRef = zipfile.ZipFile(io.BytesIO(zipData))
    zipRef.extractall(destinationPath)
    log(F"{module.id} installed")

def checkInstalledModules(modules: list, modulesFolder: str):
    pass

def createThread(module: Module, modulesFodler: str):
    return threading.Thread(target=installModule, args=(module, modulesFodler), name=module.id)

def removeDir(path):
    if os.path.isdir(path) and os.path.exists(path):
        log(f"Remove Directory {modulesFolder}")
        shutil.rmtree(path)
        log("Removed")

def log(message):
    time = datetime.datetime.now()
    print(f"{time} - {message}")

###

log('START')

platformConfigUri = sys.argv[1]
modulesFolder = sys.argv[2]

removeDir(modulesFolder)

if platformConfigUri.startswith("http"):
    log(f"Downloading from {platformConfigUri}")
    with urllib.request.urlopen(platformConfigUri) as response, open('modules.json', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
else:
    with open("modules.json", "w") as out_file:
        out_file.write(platformConfigUri)

modules = []
with open('modules.json') as f:
    config = json.load(f)
    for module in config:
        modules.append(Module(module["Id"], getModuleUrl(module["Versions"]), getModuleVersion(module["Versions"])))

checkInstalledModules(modules, modulesFolder)

threads = [createThread(module, modulesFolder) for module in modules if module.url]

for t in threads:
    t.start()
for t in threads:
    t.join()

log('INSTALL_COMPLETE')