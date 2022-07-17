from PyPDF2 import PdfFileReader


path = 'D:\\py\\Extraction_pdf\\Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf'
f = open(path, 'rb')
pdf = PdfFileReader(f)
info=pdf.getDocumentInfo()
# print(info)
# print(info.creator)
# print(info.producer)
# print(info.title)
# print(info.author)

num_pages=pdf.getNumPages()
print(num_pages)



