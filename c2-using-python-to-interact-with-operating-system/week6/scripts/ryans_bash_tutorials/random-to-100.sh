#!/bin/bash
#takes two cmd arguments (lower and upper limits)
#and returns the random int within this limits, 
#including lower and upper

let lower=$1
let upper=$2+1
echo lower: $lower
echo upper: $upper
echo ------------

#random=$(($RANDOM%$upper)) #return random from 0 to upper

random=$((($RANDOM%($upper-$lower))+$lower))
echo $random
