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
  #Run each task seperately
  subprocess.call(["rsync", "-arg", task, dest])
  print("Handling {}".format(task))

if __name__ == "__main__":
  tasks = []
  for root, dirs, files in os.walk(src):
    root_dir = root
    task = dirs
    break #breaks the loop after the first list of subdirectories in dirs
  for item in task: #iterate over the list of directories
    name = os.path.join(root_dir, item) #create path for all directories listed
    if name not in tasks:
      tasks.append(name) #populate tasks with directory paths

  with Pool(len(tasks)) as p: #Recommened handling of Pool submodule
    p.map(run, tasks)
