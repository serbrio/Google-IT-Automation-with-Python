#!/bin/bash
FILE=./testing_temp_file
n=0
while [ $n -eq 0 ]; do
	if [ -e $FILE ]
		then echo File exists:
		echo $FILE
		n=1 
	fi
done
exit 0
