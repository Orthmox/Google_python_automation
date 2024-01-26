#!/bin/bash

for log in /var/log/*log; do
	echo Processing: $log
	cut -d' ' -f5- $log | sort | uniq -c | sort -nr | head -5
	sleep 2

done
