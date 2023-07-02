#!/bin/bash
# Print message (which is all given args)
# in center of terminal

cols=$( tput cols )  # tput counts columns the terminal has
rows=$( tput lines ) # tput counts lines(rows)  the terminal has

message=$@ # All args given to script in command line

input_length=${#message} # We find out how many characters in the string message
			 # ${#@} would count how many cmd args given 

half_input_length=$(( $input_length / 2 ))

# Calculate where to place message, so that it is centered
middle_row=$(( $rows / 2 ))
middle_col=$(( ($cols / 2) - $half_input_length ))

tput clear

# Places the cursor at the given row and column.
tput cup $middle_row $middle_col 
tput bold
echo $@
# Turns bold off and any other changes, if any
tput sgr0 
# Places prompt at the bottom of the screen
tput cup $( tput lines) 0

