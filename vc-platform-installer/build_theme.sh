#!/bin/bash

THEME_REPOSITORY=$1
THEME_LOCATION=$2

git clone $THEME_REPOSITORY $THEME_LOCATION
cd $THEME_LOCATION
npm install && gulp default && gulp packJavaScript
