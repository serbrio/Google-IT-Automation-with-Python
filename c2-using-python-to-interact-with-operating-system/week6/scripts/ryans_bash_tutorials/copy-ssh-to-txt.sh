#!/bin/bash
#make a txt copy of any sh files
#in the given directory

for value in $1/*.sh
do
	cp $value $1/$( basename -s .sh $value ).txt
done
