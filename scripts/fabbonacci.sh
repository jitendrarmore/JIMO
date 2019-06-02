#!/bin/bash

a=1
b=1
echo $a
echo $b

for i in 1 2 3 4 5 6 7 9
do 
c=a
b=$a
b=$(($a+$c))
echo $b
done

