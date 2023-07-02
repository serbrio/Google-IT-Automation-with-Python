#!/bin/bash

for file in *.HTM; do
	name=$(basename "$file" .HTM)

	#echo to see|test what the script will do
	echo mv "$file" "$name.html"
done

