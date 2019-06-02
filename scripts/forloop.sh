#!/bin/bash

number=1
for i in $(ls);do
 echo "each $number item:$i"
 number=`expr $number + 1`
done 
