#!/bin/bash

# Below are examples of:
# Command to measure time used for execution of a program
# Command to profile the python script
# Command to visualize the profiler's results

time ./send_reminders.py "2222-11-11|Example-TITLE|test1,test2,test3,test4,test5,test6,test7,test8,test9"
pprofile3 -f callgrind -o profile.out ./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5,test6,test7,test8,test9"
kcachegrind profile.out 
