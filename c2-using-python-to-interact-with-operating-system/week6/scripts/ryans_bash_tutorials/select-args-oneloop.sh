#!/bin/bash
# Takes a list of arguments in command line and
# creates a simple select menu.
# Exits after one loop.

PS3="Choose one of theese: "

echo

select one
do 
	echo
	echo "You have chosen $one"
	echo
	break
done
exit 0
