#!/bin/sh
#
# Load a url (passed in argument - like chrome://gpu) into chromium and copies its contents
# to the clipboard.
# This script requires chromium window to have the focus.
#
# After this script has run, the contents of the chrome url will be
# in the clipboard. It can be retrieved with the wl-paste command
# from the wl-clipboard package.
#
# This script depends on version of ydotool >= 1.0.4
# https://github.com/ReimuNotMoe/ydotool
#
# by hector.cao@canonical.com

# key codes : /usr/include/linux/input-event-codes.h

# ydotool does not handle keyboard layout other than US
# make sure that we are having the right keyboard layout
NORMAL_UID=$(id -u ${NORMAL_USER})
sudo -H -u "${NORMAL_USER}"  DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/${NORMAL_UID}/bus \
     gsettings set org.gnome.desktop.input-sources sources "[('xkb','us')]"

# Specify where daemon and client binaries have been installed.
DAE=/usr/bin/ydotoold
YDO=/usr/bin/ydotool

# Launch the daemon and give it 2 seconds to get ready.
$DAE &
DAEMONPID=$!
sleep 2

$YDO key 29:1 20:1 20:0 29:0 # ctrl+t
sleep 1
$YDO type $1
sleep 1
$YDO key 28:1 28:0 # enter
sleep 1

# This is so nasty!
# We need to click in the right section before we can select.
# The chosed coordinates should be good, but depending on screen-resolution 
# this could actually go wrong.
# -a : absolute coordinates
$YDO mousemove -a 400 150
sleep 1
$YDO click 0xC0 # left click
sleep 1
# Select All
$YDO key 29:1 30:1 30:0 29:0 # ctrl+a
sleep 1
# Copy to clipboard
$YDO key 29:1 46:1 46:0 29:0 # ctrl+c

# Quit chromium
#$YDO key 56:1 62:1 62:0 56:0 # alt+f4

# give our key presses some time to all get through.
sleep 1

# We no longer need the ydotool daemon running, so kill it.
kill $DAEMONPID

