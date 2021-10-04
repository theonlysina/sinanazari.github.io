#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails
from reportlab.platypus import Paragraph, Spacer, Table, Image


cwd = os.getcwd()
path = "{}/{}".format(cwd, "supplier-data/descriptions")

report = Paragraph("")

if __name__ == "__main__":
        lines = []
        for file in os.listdir(path):
                dict = {}
                f, e = os.path.splitext(file)
                with open("{}/{}".format(path, file)) as fruit_file:
                        name = fruit_file.readline().strip()
                        weight =  fruit_file.readline()
                        blank = "<br/>"
                lines.append("name: " + name + "<br/>")
                lines.append("weight: " + weight + "<br/>")
                lines.append(blank)

        reports.generate_report('\tmp\processed.pdf', "Processed Update on {}".format(date.today()), lines)

        message = emails.generate_email("automation@example.com", "student-04-180d71e68f78@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "\tmp\processed.pdf")
        emails.send_email(message)
