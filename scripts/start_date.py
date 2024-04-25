#!/usr/bin/env python3
""" This was an incomplete script provided in a qwiklabs session
in module 4 in the Troubleshooting and Debugging Techniques course in
the Google Automation with python career certificate program. The 
script is modified for improved performance i.e. reduce the 
time it takes for the script to run.
"""

import csv  
import datetime
import requests
import os


FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"
file = "employee_data.csv"
file_path = os.path.abspath(file)

def get_start_date():
  """Interactively get the start date to query for."""

  print()
  print('Getting the first start date to query for.')
  print()
  print('The date must be greater than Jan 1st, 2018')
  year = int(input('Enter a value for the year: '))
  month = int(input('Enter a value for the month: '))
  day = int(input('Enter a value for the day: '))
  print()            
  
  
  
  return datetime.datetime(year, month, day)

def download_file(url):
  """Returns the lines contained in the file at the given URL"""
  
  # Download the file over the internet if file doesn't exist
  if os.path.exists(file_path):
    print("File exists. Continue!")

  else:
    print("Downloading file. Please wait.")
    response = requests.get(url, stream=True)
  
    if response.status_code == 200:  
      with open('employee_data.csv', 'wb') as f:
        f.write(response.content)
    else:
      print("Failed to download file")


def get_same_or_newer(start_date):
  """Returns the employees that started on the given date, or the closest one"""
  data = {}
  with open(file_path, 'r') as f:
    csv_data = f.read()
    reader = csv.reader(csv_data.splitlines()[1:])
    for row in reader:
      date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
      #print(date)
      if date not in data:
        data[date] = "" 
        data[date] += row[0]+" "+ row[1]
      else:
        data[date] += row[0]+" "+ row[1]
  # We want all employees that started at the same date or the closest newer
  # date. To calculate that, we go through all the data and find the
  # employees that started on the smallest date that's equal or bigger than
  # the given start date.
  min_date = datetime.datetime.today()
  min_date_employees = []
  for key in data:
    row_date = key

    # If this date is smaller than the one we're looking for,
    # we skip this row
    if row_date < start_date:
      continue

    # If this date is smaller than the current minimum,
    # we pick it as the new minimum, resetting the list of
    # employees at the minimal date.
    if row_date < min_date:
      min_date = row_date
      min_date_employees = []

    # If this date is the same as the current minimum,
    # we add the employee in this row to the list of
    # employees at the minimal date.
    if row_date == min_date:
      min_date_employees.append(data[key])
  #print(min_date)
  #print(min_date_employees)
  return min_date, min_date_employees

def list_newer(start_date):
  while start_date < datetime.datetime.today():
    start_date, employees = get_same_or_newer(start_date)
    print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

    # Now move the date to the next one
    start_date = start_date + datetime.timedelta(days=1)

def main():
  download_file(FILE_URL)
  start_date = get_start_date()
  list_newer(start_date)

if __name__ == "__main__":
  main()
