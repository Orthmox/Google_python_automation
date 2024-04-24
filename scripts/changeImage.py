#!/usr/bin/env python3
""" This script takes an image file in src and edits it. Written during a qwiklabs session
in module 4 in the Automating Real-World Tasks with Python course in
the Google Automation with python career certificate program
"""
from PIL import Image
import os


src = "/home/student/supplier-data/images"

dest = "/home/student/supplier-data/images"
exclude_files = ["README", "LICENSE"]

def edit_image():
  for item in os.listdir(src):
    #split the file name from the extension
    file, ext = os.path.splitext(item)
    #create the output file name
    output_file = file + ".jpeg"
    #ensure that no hidden files, directiores, LICENSE or README files are included
    if not item.startswith(".") and not os.path.isdir(os.path.join(src, item)) and item not in exclude_files: 
      src_file = os.path.join(src, item)
      dest_file = os.path.join(dest, output_file) #create the output file absolute path

      print("Handling {}".format(item))
      #open the file
      with Image.open(src_file) as img_file: 

      #Convert RGBA to RGB

        if img_file.mode == 'RGBA':
          img_file = img_file.convert('RGB')
          new_file = img_file.resize((600,400)) #resize the file
          new_file.save(dest_file, "JPEG")
        else:
          new_file = img_file.resize((600,400))
          new_file.save(dest_file, "JPEG")


if __name__ == "__main__":
  edit_image()
