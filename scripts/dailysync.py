#!/usr/bin/env python3
"""using rsync to backup data for src to dest employing
the Pool submodule from multiprocessing to create one process
task"""

import subprocess
import os
from multiprocessing import Pool

src = "Google_python_automation/data/prod/"
dest = "Google_python_automation/data/prod_backup/"


def run(task):
  subprocess.call(["rsync", "-arg", src, dest])
  print("Handling {}".format(task))

if __name__ == "__main__":
  tasks = []
  for root, dirs, files in os.walk(src, topdown=True):
    for name in dirs:
      task = os.path.join(root, name)
      if task not in tasks:
        tasks.append(task)
  p = Pool(len(tasks))
  p.map(run, tasks)
