#!/usr/bin/env python3

import psutil
import shutil
import email_supplier
import sys
import socket

def check_cpu():
  cpu_percent = psutil.cpu_percent(5)
  #print("Number of cores in system", psutil.cpu_count())
  #print("\nNumber of physical cores in system", psutil.cpu_count(logical=False))

  return cpu_percent


def check_mem():
  virtual_mem = psutil.virtual_memory()
  available_mem = virtual_mem.available / (1024 * 1024)
  
  return available_mem

def check_disk():
  partitions = psutil.disk_partitions()
  disk_usage = psutil.disk_usage('/')
  percent = disk_usage.percent

  return percent
def check_localhost():
  ip_address = socket.gethostbyname("localhost")

  return ip_address

def main(argv):
  From = "automation@example.com"
  To = "student@example.com"
  Subject = ""
  Body = "Please check your system and resolve the issue as soon as possible"

  if check_cpu() > 80.00:
    Subject = "Error - CPU usage is over 80%"
    message = email_supplier.generate_email(From, To, Subject, Body, attachment_path=None)
    email_supplier.send_email(message)

  if check_mem() < 100.00:
    Subject = "Error - Available memory is less than 100MB"
    message = email_supplier.generate_email(From, To, Subject, Body, attachment_path=None)
    email_supplier.send_email(message)

  if check_disk() > 80.00:
    Subject = "Error - Available disk space is less than 20%"
    message = email_supplier.generate_email(From, To, Subject, Body, attachment_path=None)
    email_supplier.send_email(message)

  if check_localhost() != "127.0.0.1":
    Subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = email_supplier.generate_email(From, To, Subject, Body, attachment_path=None)
    email_supplier.send_email(message)



if __name__ == "__main__":
  main(sys.argv)
