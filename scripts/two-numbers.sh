#!/bin/bash
# the shabong 

if [ $# -ne 2 ]
#if two inputs are not received then run below  
then
#the run below 
echo "Usage - $0 x y"
#print on the standard output how to use the script 
echo "Where x and y are two nos for which I will print sum" 
    #print on standard output, “Where x and y are two nos for which I will print sum"
exit 1
#Leave shell in Error Stage and before the task was successfully
fi
echo "sum of $1 and $2 is `expr $1 + $2`"
 
