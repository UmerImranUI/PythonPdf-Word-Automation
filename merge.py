from PyPDF2 import PdfFileReader, PdfFileWriter

paths=['Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf','newfile.pdf']
#add up as many file as u want

writer = PdfFileWriter()
print('merging files: ...')
for i in paths:
    pdf = PdfFileReader(i, 'rb')
    for page in range(pdf.getNumPages()):
        #it will iterate through all the pages
        writer.addPage(pdf.getPage(page))
        #adding pages


with open('merged.pdf', 'wb') as out:
    writer.write(out)

print('done')
