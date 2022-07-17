from PyPDF2 import PdfFileReader, PdfFileWriter


path = 'Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf'
pdf =PdfFileReader(path, 'rb')
print('splitting the pdf')

for i in range(pdf.getNumPages()):
    if i<5:  #pages splitting
        print(i)
        writer=PdfFileWriter()
        writer.addPage(pdf.getPage(i))

        output=f'page {i+1}.pdf'
        with open(output, 'wb') as out:
            writer.write(out)


print('done')


    

