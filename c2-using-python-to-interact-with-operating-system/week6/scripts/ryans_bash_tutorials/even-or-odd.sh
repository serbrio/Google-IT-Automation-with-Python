#!/bin/bash
# Prints the numbers in a line each
# and if the number is even/odd.

for number in {1..10}
do
	if (( $number % 2 == 0 ))
	then 
		echo $number EVEN
	else
		echo $number ODD
	fi
done

