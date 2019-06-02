#!/bin/bash

echo $0
echo $1
echo "script is creating to test while loop till one minutes"

n=0
while [ $n -lt 60 ]
do 
	echo "Google Hello $n"
	sleep 1
	n=`expr $n + 1` 
done
	echo "You have successfully completed the loop till 60 seconds"
 
