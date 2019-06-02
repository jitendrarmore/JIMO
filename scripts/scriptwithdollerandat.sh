#!/bin/bash

echo "Using \$\@:"

for i in "$@";
do 
	echo $i 
done

