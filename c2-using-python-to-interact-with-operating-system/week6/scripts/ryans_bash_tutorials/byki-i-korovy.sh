#!/bin/bash
# Command line version of the game Mastermind or Code Braker.

echo ==============================================
echo Biky i korovy
echo
echo Given: 12345678
echo Guess right digits and their correct order. 
echo You have 8 chances.
echo ==============================================

code=$( shuf -e 1 2 3 4 5 6 7 8 | head -n 5 | tr -d '[:space:]' )


counter=1
while [ $counter -le  8 ]
do
	echo 
	echo Try No: $counter
	echo Enter your guess in format: 12345
	read -p "Your guess: " guess
	case "$guess" in
		code)
			echo Congratulations! You got it!
			break
			;;
	esac
	guessed_digits=0
	correct_order=0
	for digit in {0..4}
	do
		if [ ${guess:$digit:1} == ${code:$digit:1} ]
		then
			(( correct_order++ ))
			(( guessed_digits++ ))
		elif [ "$(echo $code | grep $digit)" ]
		then
			(( guessed_digits++))
		fi

	done
	echo Guessed digits: $guessed_digits
	echo On correct places: $correct_order
	(( counter++ ))
done

echo ==================================
echo Cheer up!
echo The code was: $code
echo Your last guess was: $guess
echo Do not take it close to your heart!
echo And try again.
echo ===================================
