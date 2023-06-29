#!/bin/bash
# A simple menu system 

names='Quit Robin Batman Freezer Miles'

PS3='Select character: ' # The system $PS3 var (prompt) is changed

select name in $names
do
	if [ $name == 'Quit' ]
	then 
		break
	fi
	echo Hello $name
done

echo Bye
