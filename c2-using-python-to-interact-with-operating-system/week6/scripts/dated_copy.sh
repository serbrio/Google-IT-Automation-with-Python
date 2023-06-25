#!/bin/bash

#dated_name=$(date +%Y-%m-%d)_$1
ext=$(basename $1 | grep -oP "^.+\K\.[a-zA-Z0-9]+$")
name=$(basename -s $ext $1)_
dated_name=$name$(date +%Y-%m-%d)$ext
echo "ext: $ext"
echo "name: $name"
echo "dated_name: $dated_name"
cp $1 $dated_name
