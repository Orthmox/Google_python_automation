#!/bin/bash
file=$(grep "jane " ../data/list.txt | cut -d' ' -f3)
for i in $file; do echo ..$i; done
