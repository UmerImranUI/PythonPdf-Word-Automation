from tkinter import N
from pdf2docx import Converter, parse

pdf_file='page 1.pdf'
word_file='demo.docx'

#converter method
# cv=Converter(pdf_file)
# cv.convert(word_file, start=0, end=None)
# cv.close()

#parse method
parse(pdf_file, word_file, start=0, end=None)
