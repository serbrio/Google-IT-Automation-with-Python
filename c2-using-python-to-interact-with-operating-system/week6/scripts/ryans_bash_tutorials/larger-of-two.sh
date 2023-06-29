#!/bin/bash
#take two numbers as args and print the larger of two 

if [ $1 -gt $2 ]
then 
	echo $1
else 
	echo $2
fi
