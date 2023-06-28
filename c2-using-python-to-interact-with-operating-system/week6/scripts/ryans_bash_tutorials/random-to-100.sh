#!/bin/bash

lower=$1
upper=$2

random=$((($RANDOM+$lower)%$upper))
echo $random
