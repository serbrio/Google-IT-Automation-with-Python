#!/bin/bash

echo $@ | basename -s .txt -a *.txt | xargs -i cp {}.txt {}_$(date +%Y-%m-%d).txt
