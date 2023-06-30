#!/bin/bash
# Takes a one command line argument (directory) and
# prints each entry of it.
# If the entry is a file - prints it's size,
# If the entry is a dir - prints how many items there are in that dir.
# And prints if nicely, using printf.

for item in $1/*
do
	if [ -d "$item" ]
	then
		items_count=$( ls "$item" | wc -l )
		printf '%-6s %s\n' "$items_count" "$item"
	elif [ -e "$item" ]
	then
		file_size=$( du -h "$item" | awk '{ print $1 }' )
		printf '%-6s %s\n' "$file_size" "$item"
	fi
done
