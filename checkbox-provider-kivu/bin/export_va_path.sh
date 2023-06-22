#!/bin/bash

if [ "$0" = "$BASH_SOURCE" ]; then
    echo "Error: Script must be sourced"
    exit 1
fi

SCRIPT_PATH="$(dirname -- "${BASH_SOURCE[0]}")"

# We want the validate VA-API features of chromium, so use VA drivers from chromium and gnome sdk
# We do not want to use the host's librairies

GNOME_SDK=$(${SCRIPT_PATH}/detect-gnome.sh)
# libva
export LD_LIBRARY_PATH=/snap/${GNOME_SDK}/current/usr/lib/x86_64-linux-gnu:/snap/chromium/current/usr/lib/x86_64-linux-gnu/
# intel media driver backend
export LIBVA_DRIVERS_PATH=/snap/${GNOME_SDK}/current/usr/lib/x86_64-linux-gnu/dri/
