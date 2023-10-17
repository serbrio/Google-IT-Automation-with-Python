#!/bin/bash

# This script runs ffmpeg in parallel to convert all the webm files to mp4.
echo "Starting video conversion"
for video in some_folder/*.webm; do
	mp4_video="$(echo "$video" | sed 's/\.webm$/.mp4/')"
	daemonize -c $PWD /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video"
done
