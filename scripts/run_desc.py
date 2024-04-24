#!/usr/bin/env python3
""" This script takes data in a text file in src proccess it into a dictionary
  and uploads it to url and prints a message on the terminal depending on the
 success of the uplaod. Written during a qwiklabs sessionin module 4 in the
 Automating Real-World Tasks with Python course inthe Google Automation with
 python career certificate program
"""
import os
import locale
import requests

#variables to store src and url
src = "/home/student/supplier-data/descriptions"
url = "http://34.148.65.89/fruits/"


def post_desc():
  for item in os.listdir(src): #get a list of items in src
    if item.endswith(".txt"): #must be a text file
      file, ext = os.path.splitext(item) #split file name from extension
      src_file = os.path.join(src, item) #create file abs path


      image_name = item.replace("txt", "jpeg") #create image name for image
        #to be associated with file

      print("Handling {}".format(item))

      #open file in read mode
      with open(src_file, 'r') as file:
        data_list = []

        for line in file: #append each line as an element in a list
          data_list.append(line)

        #make the weight value a float
        weight_strp = data_list[1].strip()
        weight_lbs = locale.atof(weight_strp.strip("lbs"))
        #create a dictionary
        data_dict = {
          "name": data_list[0].strip(),
          "weight": weight_lbs,
          "description": data_list[2].strip(),
          "image_name": image_name
        }

      #make a post to the url with the dictionary as data in json format
      response = requests.post(url, json=data_dict)


      if response.status_code == 201:
        print("Post {} complete".format(item))
      else:
        print("Post {} failed".format(item))





if __name__ == "__main__":
  post_desc()
