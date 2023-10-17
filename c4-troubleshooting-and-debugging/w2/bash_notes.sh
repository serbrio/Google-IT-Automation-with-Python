#!/bin/bash

# This piece of code CONTinues every singe stopped ffmpeg process (by pid)
# one after another, if the previous one has finished.
for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done
