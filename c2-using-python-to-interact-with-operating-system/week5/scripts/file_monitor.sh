#!/bin/bash
FILE=$1
echo Wating for file: $1
n=0
while [ $n -eq 0 ]; do
	if [ -e $FILE ]
		then echo File exists:
		echo $FILE
		n=1 
	fi
done
exit 0
