#!/bin/bash

# generate a video from video pattern with given nb of repetition

SCRIPT_PATH=$(readlink -f "${BASH_SOURCE:-$0}")
DIR_PATH=$(dirname $SCRIPT_PATH)

# input video to repeat (must be absolute path)
INPUT_FILE=$1
# nb of repeats
NB_REPEAT=$2
# output file
OUTPUT_FILE=$3

if [ -z "${OUTPUT_FILE}" ]; then
    exit 1
fi

# look for gnome-screenshot
if [ ! -x "$(which ffmpeg)" ]; then
  echo "Missing ffmpeg"
  exit 0
fi

# must be relative to current exec folder
PLAINBOX_SESSION_SHARE=${PLAINBOX_SESSION_SHARE:-/tmp/}
FFMPEG_INPUT_FILE="${PLAINBOX_SESSION_SHARE}inputs-2fe6488a-ccba-11ed-afa1-0242ac120002.txt"

rm -f ${FFMPEG_INPUT_FILE}

# need ffmpeg package
for ((i = 1; i <= "${NB_REPEAT}"; i++)); do
    echo "file '${INPUT_FILE}'" >> ${FFMPEG_INPUT_FILE}
done

rm -f ${OUTPUT_FILE}
# -safe 0 : avoid 'unsafe filename error' 
ffmpeg -f concat -safe 0 -i ${FFMPEG_INPUT_FILE} -c copy ${OUTPUT_FILE}
