#!/bin/bash

THEME_URL=$1
THEME_LOCATION=$2

if [ ! -d "$THEME_LOCATION" ]; then
    mkdir -p "$THEME_LOCATION"
fi

DOWNLOAD=$(date +%Y-%m-%d-%H-%M-%S).zip
wget -O $DOWNLOAD $THEME_URL
mkdir temp
unzip -o $DOWNLOAD -d temp
cd temp && mv $(ls -td -- * | head -n 1) temp_theme && cp -rp temp_theme/* $THEME_LOCATION && cd .. && rm -rf temp