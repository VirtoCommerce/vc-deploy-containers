import sys
import datetime
import os
import urllib.request 
import glob
import shutil
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

pageBuilderPath = 'content/'
tmpPath = '/tmp/page-builder-theme/'
settingsPath = 'config/settings_data.json'

themeUrl = sys.argv[1]
themeFolder = sys.argv[2]
installed_theme_file = os.path.join(themeFolder, 'installed_theme.txt')
from zipfile import ZipFile

def download_theme():
    print(datetime.datetime.now())
    print('Downloading theme from:', themeUrl)
    url = themeUrl
    urllib.request.urlretrieve(url, "theme.zip")
    print(datetime.datetime.now())
    print('Theme successfuly downloaded!')
    with ZipFile('theme.zip', 'r') as zipObject:
        listOfFileNames = zipObject.namelist()
        for fileName in listOfFileNames:
                zipObject.extract(fileName, themeFolder)
                print('Extraction...', fileName) 
    installed_theme = open(installed_theme_file, 'w')
    text_for_file = themeUrl
    installed_theme.write(text_for_file)
    os.remove('theme.zip')

def copy_content(from_path, to_path):
    print(datetime.datetime.now())
    print('Copying Page Builder content...')
    from_folder = os.path.join(from_path, pageBuilderPath)
    to_folder = os.path.join(to_path, pageBuilderPath)
    if(os.path.exists(from_folder)):
        copy_tree(from_folder, to_folder)
        print(datetime.datetime.now())
    settingsFileFrom = os.path.join(from_path, settingsPath)
    settingsFileTo = os.path.join(to_path, settingsPath)
    if(os.path.exists(settingsFileFrom)):
        copy_file(settingsFileFrom, settingsFileTo)
    print('Copying complete')

def removing_old_theme(path):
    print(datetime.datetime.now())
    print('Removing old theme...')
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

if(os.path.exists(installed_theme_file)):
    check_theme_version = open(installed_theme_file, 'r')
    current_version = check_theme_version.read()
    if current_version != themeUrl:
        copy_content(themeFolder, tmpPath)
        removing_old_theme(themeFolder)
        download_theme() 
        copy_content(tmpPath, themeFolder)
        removing_old_theme(tmpPath)
    else:
        print('Theme up to date')
else:
    copy_content(themeFolder, tmpPath)
    removing_old_theme(themeFolder)
    download_theme()
    copy_content(tmpPath, themeFolder)

