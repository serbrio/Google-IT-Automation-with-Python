#!/bin/bash
#Catch all "jane" lines and store them in text file oldFiles.txt

files=$(grep 'jane ' ../data/list.txt | cut -d ' ' -f 3)
> oldFiles.txt

for file in $files; do
	if [ -e "..$file" ]
	then
		echo ..$file >> oldFiles.txt 
	fi
done
