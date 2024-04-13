#!/usr/bin/env python3          

""" This script takes feedback stored in a text file and posts it to a website"""

import os
import requests

#store the absolute path of the feedback directory in a variable
src = "/home/orthmox/Desktop/Google_python_automation/data/feedback" 

def post_feedback():
  for file in os.listdir(src):  #iterate throug the files in the directory
    src_file = os.path.join(src, file) #create the absolute path of the file
    print("Handling {}".format(file))

    with open(src_file, 'r') as text: #open the file and create and empty list to store the the content per line of the file
      feed_list = []
      feed_dict = {}
      for line in text:
        feed_list.append(line)
      #store the content of the file a dictionary as "title", "name", "date" and "feedback"
      feed_dict = { 
        "title": feed_list[0].strip(), 
        "name": feed_list[1].strip(),
        "date": feed_list[2].strip(),
        "feedback": feed_list[3].strip()
      }
    response = requests.post(url, json=feed_dict) #post the feedback to the website
    #JSON directly converts dictionary to json format
    #print(response.status_code) #prints status code
    #print(response.request.url) #prints the url where the feedback was posted
    #print(response.request.body) #prints the body of the http request


    if response.status_code == 200 or response.status_code == 201:
      print("Succcessfully posted feedback @ {}".format(file))
    else:
      print("Failed to post feedback @ {}".format(file))

if __name__ == "__main__":
  post_feedback()



















