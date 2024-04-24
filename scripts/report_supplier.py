#!/usr/bin/env python3
""" This script is  a version of the reports.py script provided in a qwiklabs session
in module 3 in the Automating Real-World Tasks with Python course in
the Google Automation with python career certificate program that generates a pdf file
with data in table format(does not include pie chart)
"""
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet() #get styles for pdf content
  report = SimpleDocTemplate(filename) #create file with .pdf extension
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info]) #generate pdf file
