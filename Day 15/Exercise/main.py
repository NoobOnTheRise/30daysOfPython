"""
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

"""
import os
from PyPDF2 import PdfWriter

merger = PdfWriter()
files = os.listdir("exercise")

for pdf in files:
  file = "exercise/" + pdf
  merger.append(file)

merger.write("exercise/merged-pdf.pdf")
merger.close()
