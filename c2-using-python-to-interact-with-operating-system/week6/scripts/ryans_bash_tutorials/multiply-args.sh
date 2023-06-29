#!/bin/bash

let multi=$1*$2
echo 1: $multi

let "multi = $1 * $2"
echo 2: $multi

echo 3: "expr \$1 \* \$2"
expr $1 \* $2

multi=$( expr $1 \* $2)
echo 4: $multi

multi=$(($1*$2))
echo 5:  $multi

multi=$(( $1 * $2 ))
echo 6: $multi

echo 7: "(( \$1 * \$2 ))"
echo $(($1 * $2))
