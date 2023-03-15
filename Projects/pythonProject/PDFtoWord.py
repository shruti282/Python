import PyPDF2
from PyPDF2 import PdfReader
import sys
import os

path = "D:\Python\PDFtoWord"
filename = os.listdir(path)

with open(filename, mode='rb') as f:
    reader = PyPDF2.PdfReader(f)
    page = reader.pages[0]
    print(page.extract_text())
