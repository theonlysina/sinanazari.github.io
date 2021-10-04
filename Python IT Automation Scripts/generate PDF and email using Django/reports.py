#!/usr/bin/env python3

from datetime import date
import reports
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
        str = ""
        # str += "<br/>"
        for i in range(len(paragraph)):
                str += paragraph[i]
               # str += "<br/>"
               # if i % 2 == 0 and i != 0:
               #         str += "<br/><br/>"

        report = SimpleDocTemplate(attachment)
        styles = getSampleStyleSheet()
        title2 = Paragraph("Processed Update on {}".format(date.today()), styles["h1"])
        empty_line = Spacer(1,20)
        report_data = Paragraph(str, styles["Normal"])
        report.build([title2, empty_line, report_data])

