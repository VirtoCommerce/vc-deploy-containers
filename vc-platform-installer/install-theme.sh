#!/bin/bash

THEME_URL=$1
THEME_LOCATION=$2

if [ ! -d "$THEME_LOCATION" ]; then
    mkdir -p "$THEME_LOCATION"
fi

wget -O theme.zip $THEME_URL
DOWNLOAD=$(date +%Y-%m-%d-%H-%M-%S).zip
mv theme.zip $DOWNLOAD
unzip $DOWNLOAD
cp -rp $(ls -t -1r | tail -1)/* $THEME_LOCATION