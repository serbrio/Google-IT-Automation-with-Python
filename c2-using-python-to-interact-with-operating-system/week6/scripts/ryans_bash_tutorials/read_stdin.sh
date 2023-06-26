#!/bin/bash

#echo Here will be shown the first, third and fifth words from stdin
echo
echo ================================================
echo

#cat /dev/stdin | cut -d " " -f 1,3,5
cat /dev/stdin | head -n 3 | tail -n 1 
