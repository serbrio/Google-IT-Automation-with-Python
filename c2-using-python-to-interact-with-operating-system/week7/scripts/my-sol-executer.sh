#!/bin/bash

command=$1
n=1
while true; do #later try: while $command:
	cat test_logs.txt | grep " ticky: " | $command &>>bashlog_first.txt
	echo "Retry #$n DONE!"
	((n++))
	sleep 10
done;