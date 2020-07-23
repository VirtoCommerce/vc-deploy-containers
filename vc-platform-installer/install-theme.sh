#!/bin/bash

THEME_URL=$1
THEME_LOCATION=$2

wget -O theme.zip $THEME_URL
unzip theme.zip
cp -rp default/* $THEME_LOCATION
