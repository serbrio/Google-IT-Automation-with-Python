#!/bin/bash
#print a message about disk usage

space_free=$( df -h | awk '{ print $5 }' | sort -n | tail -n 1 | sed 's/%//' )

case $space_free in
	[1-5]*)
		echo PLenty disk space available
		;;
	[6-7]*)
		echo There could be a problem in the near future
		;;
	8*)
		echo Maybe we should clear old files
		;;
	9*)
		echo We could have a serious problem soon
		;;
	*)
		echo Something is not quite right here
		;;
esac
