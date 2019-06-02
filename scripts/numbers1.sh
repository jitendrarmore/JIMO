#!/bin/bash

if [ $# -ne 1 ]
then 
	echo " please provide the argument"
	exit 1
fi

n=$1
reverse=0
sigledigit=0

while [ $n -gt 0 ]
do
	sigledigit=`expr $n % 10`
	reverse=`expr $reverse \* 10 + $sigledigit`
	n=`expr $n / 10`
done
	echo "Reverse number is $reverse"


