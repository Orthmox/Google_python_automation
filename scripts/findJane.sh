#!/bin/bash
> oldFiles.txt

files=$(grep "jane " ../data/list.txt | cut -d' ' -f3)

for i in $files; do while test -e ../
