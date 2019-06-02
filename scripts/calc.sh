#!/bin/bash
NAME=$@
money=500
echo Day Salary "$money" 
Monthly=`echo "calculating of monthly $(($money * 30)) PM"`
echo $1 $2 $Monthly
echo $1 $2 "Yearly salary = $(($money * 30 * 12)) PM"
echo $$
echo $NAME

