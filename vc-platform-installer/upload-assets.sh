#!/bin/sh

ASSETS_URL=$1
ASSETS_LOCATION=$2

if [ ! -d "$ASSETS_LOCATION" ]; then
     mkdir -p "$ASSETS_LOCATION"
     wget -O assets.zip $ASSETS_URL
     unzip assets.zip
     cp -rp assets/* $ASSETS_LOCATION
fi
 echo "Assets already installed"
