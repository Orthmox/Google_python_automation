#!/usr/bin/env python3
""" This script is a copy of the emails.py script provided in a qwiklabs session
in module 3 in the Automating Real-World Tasks with Python course in
the Google Automation with python career certificate program
"""
import email.message
import os
import mimetypes
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path):

  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  if attachment_path:
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1) 

    with open(attachment_path, 'rb') as file:
      message.add_attachment(file.read(), maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)


  return message


def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()


