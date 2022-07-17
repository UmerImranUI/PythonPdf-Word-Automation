from PyPDF2 import PdfFileReader, PdfFileWriter


path = 'Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf'
pdf =PdfFileReader(path, 'rb')
writer=PdfFileWriter()
writer.addPage(pdf.getPage(4))
writer.addPage(pdf.getPage(5))

with open('newfile.pdf','wb') as out:
    writer.write(out)