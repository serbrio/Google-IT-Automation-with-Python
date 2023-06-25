#!/bin/bash

lines=1
words=/usr/share/dict/words

if [[ ! -z $1 && $1 =~ ^[0-9]+$ ]]; then
	random_word=$( cat $words | grep -e "^.\{$1\}$"  )
else
	random_word=$( cat $words | sort -R | head -n $lines  )
fi

echo "Random word(s): "
echo "$random_word"
