#!/bin/bash
#print funny message based on the current
#day of the week

weekday=$( date +%A )

case $weekday in
	понедельник)
		echo "Monday is a hard day, as they say."
		echo "They say a lot though."
		;;
	вторник)
		echo "Tuesday - do I spell it correctly?"
		;;
	среда)
		echo "Wednesday: the middle."
		;;
	четверг)
		echo "Thursday: one day before Friday!"
		;;
	пятница)
		echo "Friday: everybody ready to leave town."
		;;
	*)
		echo "This is weekend, my dear!"
		;;
esac
