#!/usr/bin/env python3

from PIL import Image
import os

src = "/home/orthmox/Desktop/Google_python_automation/images"
dest = "/home/orthmox/Desktop/Google_python_automation/opt/icons/"

def edit_image():
  for item in os.listdir(src):
    #ensure that no hidden files or directories as included
    if not item.startswith(".") and not os.path.isdir(os.path.join(src, item)): 
      src_file = os.path.join(src, item)
      dest_file = os.path.join(dest, item)
      print("Handling {}".format(item))

      with Image.open(src_file) as img_file: 
      #the following conversion is necessary as saving some files directly in JPEG raises error
        if img_file.mode == 'LA':
          img_file = img_file.convert('RGB')
          new_file = img_file.rotate(90).resize((128,128)) #rotating 90 results in an upside down image
          new_file.save(dest_file, "jpeg")

        elif img_file.mode == 'L':
          img_file = img_file.convert('RGBA')
          new_file = img_file.rotate(90).resize((128,128)) #this passes the check
          new_file.save(dest_file, "jpeg")

        elif img_file.mode == 'P':
          img_file = img_file.convert('RGB')
          new_file = img_file.rotate(90).resize((128,128)) #but could rotate 270 for better viewing
          new_file.save(dest_file, "jpeg")

        else:
          new_file = img_file.rotate(90).resize((128,128))
          new_file.save(dest_file, "jpeg")

if __name__ == "__main__":
  edit_image()
