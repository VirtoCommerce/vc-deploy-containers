#!/bin/bash

ASSETS_URL=$1
ASSETS_LOCATION=$2


wget -O assets.zip $ASSETS_URL
unzip assets.zip
cp -rp assets/* $ASSETS_LOCATION
