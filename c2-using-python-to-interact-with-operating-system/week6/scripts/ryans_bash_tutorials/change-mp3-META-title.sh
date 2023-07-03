#!/bin/bash
# Change the title in metadata of mp3 files 
# in all mp3 files in the given in command line dir,
# which fit the regex

files="$1*"

for file in $files; do
	title=$(basename -s .mp3 "$file" | grep -oP "^[0-9]+[ _.-]*\K[a-zA-Zа-яА-Я]+.*$")
       	# | iconv -t utf-8)
	#title=$(echo "$title" | grep -oP ".*(?=\.mp3)")
	if [ "$title" ]
	then
		id3v2 -t "$title" "$file"
	fi
done
