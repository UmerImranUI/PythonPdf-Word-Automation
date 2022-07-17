from PyPDF2 import PdfFileReader, PdfFileWriter


path = 'D:\\py\\Extraction_pdf\\Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf'
pdf = PdfFileReader(path) #reads file
writer= PdfFileWriter() #writer obj

for i in range(pdf.getNumPages()):
    #run by total no. of pages
    page=pdf.getPage(i)
    writer.addPage(page)
    #adding pages to the objon

writer.encrypt(user_pwd='pass@123', owner_pwd=None, use_128bit=True)
#encryption

with open('encrypt.pdf', 'wb') as out:
    writer.write(out)