#!/usr/bin/env python3
# This script capitalizes words taken from stdin
# It is used instead of hard reading bash:
# for i in $(cat story.txt); do B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; echo -n "${B}${i:1} "; done; echo -e "\n"


import sys

for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.capitalize() for word in words]))

