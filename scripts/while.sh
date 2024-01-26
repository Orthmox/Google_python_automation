#!/bin/bash

n=1
while [ $n -le 5 ]; do
	echo "Count $n"
	((n+=1))
done
