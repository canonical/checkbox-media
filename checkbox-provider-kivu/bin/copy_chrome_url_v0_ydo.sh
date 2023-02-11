#!/bin/sh
#
# Load an url like chrome://gpu into chromium and copies its contents
# to the clipboard.
#
# This script depends on a pre 1.0-version of ydotool
# https://github.com/ReimuNotMoe/ydotool
# 
# The version currently in Ubuntu 22.10 will work.
# The version currently upstream is too new, and has changed syntax.
#
# To run this with v1 or higher of ydotool, we need to use key codes
# like 29:1 for ctrl key down, and 56:0 for alt key up.
# In addition, we need to be running the daemon too.
#
# After this script has run, the contents of the chrome url will be
# in the clipboard. It can be retrieved with the wl-paste command
# from the wl-clipboard package.
#
# by bram.stolk@canonical.com

# Specify where daemon and client binaries have been installed.
#DAE=/usr/bin/ydotoold # Not req'd for ydotool v0
YDO=/usr/bin/ydotool

# Launch the daemon and give it a second to get ready.
# (Skipped in this script.)
#$DAE &
#DAEMONPID=$!

sleep 1

# Open browser tab via Ctrl+t
$YDO key ctrl+t

# Browse to the chrome url
$YDO type $1
$YDO key enter

sleep 1

# This is so nasty!
# We need to click in the right section before we can select.
# The chosed coordinates should be good, but depending on screen-resolution 
# this could actually go wrong.
$YDO mousemove 300 300
$YDO click left

# Select All
$YDO key ctrl+a

# Copy to clipboard
$YDO key ctrl+c

# Quit chromium
$YDO key alt+F4

# give our key presses some time to all get through.
sleep 1

# We no longer need the ydotool daemon running, so kill it.
#kill $DAEMONPID

