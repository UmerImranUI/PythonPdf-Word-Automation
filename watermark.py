from PyPDF2 import PdfFileReader, PdfFileWriter


path = 'D:\\py\\Extraction_pdf\\Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf'
pdf = PdfFileReader(path) #reads file
writer= PdfFileWriter() #writer obj

water=PdfFileReader('umerr.pdf') 
watermark = water.getPage(0) #watermark

for i in range(pdf.getNumPages()):
    #run by total no. of pages
    page=pdf.getPage(i)
    page.mergePage(watermark) #merging watermark to page
    writer.addPage(page)
    #writes the data

with open('waterm.pdf', 'wb') as out:
    writer.write(out)