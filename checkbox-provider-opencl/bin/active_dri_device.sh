#!/bin/sh
#
# This script uses the gfxi tool to see which dri device is active.
# This is useful when you have an iGPU and dGPU and want to know
# which one is currently driving a screen.
#
# By bram.stolk@canonical.com

crtc_card_0=`GFXI_DEVICE=/dev/dri/card0 gfxi crtc ACTIVE:1`
if [ -n "$crtc_card_0" ]; then
  echo /dev/dri/card0
  exit 0
fi

crtc_card_1=`GFXI_DEVICE=/dev/dri/card1 gfxi crtc ACTIVE:1`
if [ -n "$crtc_card_1" ]; then
  echo /dev/dri/card1
  exit 0
fi

crtc_card_2=`GFXI_DEVICE=/dev/dri/card2 gfxi crtc ACTIVE:1`
if [ -n "$crtc_card_2" ]; then
  echo /dev/dri/card2
  exit 0
fi

exit 1

