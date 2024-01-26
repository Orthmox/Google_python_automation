#!/bin/bash
# Get the absolute path of the directory containing the script
script_dir=$(dirname "$(readlink -f "$0")")
> oldFiles.txt

files=$(grep "jane " ../data/list.txt | cut -d' ' -f3)

for i in $files; do 
  if test -e ..$i; then
  echo $script_dir$i >> oldFiles.txt;
  fi
done
