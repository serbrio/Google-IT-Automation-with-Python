#!/bin/bash
# A function with a  simple menu system, which takes a list of arguments.
# Breaks after the first execution.

PS3='Select your favourite vegetable: ' # The system $PS3 var (prompt) is changed

echo

choice_of()
{
select vegetable
	# No [in list], so 'select' uses the arguments given to function 
do
	echo Hello
	echo "You prefer $vegetable."
	echo ";-)"
	echo
	break
done
}

choice_of beans rice carrot tomato cabbage broccoli pumpkin 

exit 0
