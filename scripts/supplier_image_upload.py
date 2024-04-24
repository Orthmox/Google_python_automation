#!/usr/bin/env python3
"""This script takes jpeg files in the src directory and uploads it to
the url and prints out a message to the terminal depending on the 
success of the upload
"""
import requests
import os


url = "http://localhost/upload/"
src = "/home/student/supplier-data/images"

def upload_image():

  for item in os.listdir(src):
    if item.endswith(".jpeg"):
      src_file = os.path.join(src, item)
      with open(src_file, 'rb') as image:
        print("Uploading {}".format(src_file))
        response = requests.post(url, files={'file': image})

        if response.status_code == 201:
          print("Upload complete")
        else:
          print("Upload failed")


if __name__ == "__main__":
  upload_image()
