#!/bin/bash

COUNTER=20
until [ $COUNTER -lt 10 ]
do 
	echo "The counter is $COUNTER "
	let COUNTER=COUNTER-1
done

