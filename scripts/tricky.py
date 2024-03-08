#!/usr/bin/env python3
"""#failed checks while submitting work. Reason: files created from preceeding exercise were missing. Solution: did preceeding exercises to create needed files. PROBLEM SOLVED!!"""
import re
import sys
import operator
import csv

file = '/home/orthmox/Desktop/trysyslog.log'
def create_user_stats(filename):
  user_stats = {}
  with open(filename, 'r') as f:
    user_name_pattern = r"\((\w.*)\)"
    for line in f:
      match = re.search(user_name_pattern, line)
      if match:
        user_name = match[1]
        if user_name not in user_stats:
          user_stats[user_name] = {'Username': user_name, 'INFO': 0, 'ERROR': 0}
        if "INFO" in line:
          user_stats[user_name]['INFO'] += 1
        elif "ERROR" in line:
          user_stats[user_name]['ERROR'] += 1
  user_data =[] #initialize empty list to store user data
  for user in user_stats: 
    user_data.append(user_stats[user]) #iterate over keys in the dictionary and append values to list
  sort = sorted(user_data, key=lambda x: x['Username']) #sort list by username
  keys = ["Username", "INFO", "ERROR"]
  with open('user_statistics.csv', 'w') as user_csv:
    writer = csv.DictWriter(user_csv, fieldnames=keys)
    writer.writeheader()
    writer.writerows(sort)

def error_messages(filename):
  errors = {}
  with open(filename, 'r') as f:
    errorm_pattern = r"(ERROR) ([^\(]+)"
    for line in f:
      result = re.search(errorm_pattern, line)
      if result:
        error_message = result.group(2)
        stripped_message = error_message.strip()
        if stripped_message not in errors:
          errors[stripped_message] = 0
          errors[stripped_message] += 1
        elif stripped_message in errors:
          errors[stripped_message] += 1
      else:
        continue
  error_count = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
  #write error_message.csv file
  with open('error_message.csv', 'w') as error_csv:
    writer = csv.writer(error_csv)
    writer.writerow(['Error', 'Count'])
    writer.writerows(error_count)

def main():
  file = 'trysyslog.log'
  file1 = 'trysyslog.log'
  error_messages(file)
  create_user_stats(file1)

if __name__ == "__main__":
  main()
