#!/bin/bash

THEME_URL=$1
THEME_LOCATION=$2

if [ ! -d "$THEME_LOCATION" ]; then
    mkdir -p "$DIR"
fi

wget -O theme.zip $THEME_URL
unzip theme.zip
cp -rp default/* $THEME_LOCATION
