#!/bin/bash

GNOME=$(snap connections chromium | grep -Po 'gnome(-\d+)+')
if [ -z "GNOME" ]; then
    exit 1
fi

# GNOME contains multiple instances of gnome-xx, take only the first one
set -- $GNOME

echo $1
