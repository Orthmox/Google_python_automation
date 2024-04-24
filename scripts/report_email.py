#!/usr/bin/env python3
""" This script creates a pdf file from data in src and sends it as an attachment
in an email. Written during a qwiklabs session in module 4 in the Automating 
Real-World Tasks with Python course inthe Google Automation with python career 
certificate program
"""
import report_supplier
import os
import datetime
import sys
import email_supplier

#process the data
def process_data(src_dir):
  today = datetime.date.today()
  today_str = today.strftime("%a, %B %d, %Y")
  data = []
  
  for item in os.listdir(src_dir):
    if item.endswith(".txt"):
      src_file = os.path.join(src_dir, item)

      with open(src_file, 'r') as text:
        temp = []
        for line in text:
          temp.append(line.strip())
        data += "name: "+temp[0], "weight: "+temp[1]+"<br/>" #<br/> pushes next data entry
          #to a new line in the pdf file

  return data

def main(argv):
  src = "/home/orthmox/Desktop/Google_python_automation/data/supplier-data/descriptions"
  today = datetime.date.today() #get today's date
  today = today.strftime("%B %d, %Y") #format it in month_name day, year
  title = "Processed Update on {}".format(today) 
  file = "/home/orthmox/Desktop/Google_python_automation/data/processed.pdf"
  data = process_data(src)
  summary = '<br/> '.join(data) #create a string from data seperated by a line break
  print(summary)
  #print(data)
  
  #generate report
  report_supplier.generate_report(file, title, summary)
  #compose email message
  From = "automation@example.com"
  To = "student@example.com"
  Subject = "Upload Comopleted - Online Fruit Store"
  Body = "All fruits are uploaded to our website successfully. A detailed lit is attached to this email."
  Attachment = file

  message = email_supplier.generate_email(From, To, Subject, Body, Attachment)
  #send email
  email_supplier.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
