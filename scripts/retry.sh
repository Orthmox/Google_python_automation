#!/bin/bash

n=0
command=$1
#call with random exit as argument
while ! $command && [ $n -le 5 ]; do
	sleep $n
	((n+=1))
	echo "Retry #$n"

done
