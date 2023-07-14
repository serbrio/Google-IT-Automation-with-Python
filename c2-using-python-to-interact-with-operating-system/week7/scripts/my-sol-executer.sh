#!/bin/bash

command=$1
command2="./csv_to_html.py"
n=1
while true; do
	cat test_logs.txt | grep " ticky: " | $command &>>bashlog_first.txt
	echo "Retry #$n DONE!"
	((n++))
	echo "exit code: $?" &>>bashlog_first.txt
	if [ $? == 0 ]; then
		$command2 "err.csv" "err.html" &>>bashlog_first.txt
		$command2 "stat.csv" "stat.html" &>>bashlog_first.txt
fi
	sleep 10
done; 