import PyPDF2

f=open('D:\\py\\Extraction_pdf\\Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf','rb')


pdf=PyPDF2.PdfFileReader(f)

# print(pdf.numPages)
page= pdf.getPage(0)

#can't read correctly or even can't read some pdfs due to encoding
print(page.extractText())
f.close()