#!/bin/bash

echo " checking if file exist or not"
a="$*"

if [ -f$a ]
then 
echo "file exits"
else
echo "file is not exist"
fi
