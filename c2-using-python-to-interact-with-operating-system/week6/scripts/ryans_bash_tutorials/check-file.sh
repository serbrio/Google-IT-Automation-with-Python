#!/bin/bash
#take file (path to file) as argument 
#and check if it is executable or writable

if [ -x $1 ] || [ -w $1 ]
then 
	echo "File $1 is executable or writable"
else
	echo "File $1 is not executable nor writable"
fi

