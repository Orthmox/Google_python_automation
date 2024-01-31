#!/usr/bin/env python3

import sys
import subprocess

file = sys.argv[1]

oldstring = ""
newstring =""
with open(file) as f:
  for line in f:
    oldstring = line.strip()
    newstring = oldstring.replace("jane", "jdoe")
    print(oldstring)
    print(newstring)
    subprocess.run(["mv", oldstring, newstring])
