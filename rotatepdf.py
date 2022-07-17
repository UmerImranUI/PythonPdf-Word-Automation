import PyPDF2

input=open('D:\\py\\Extraction_pdf\\Literature__Presidents_Club_Excellence_Award_Winners_Booklet.pdf','rb')

pdf=PyPDF2.PdfFileReader(input)
writer=PyPDF2.PdfFileWriter()

page=pdf.getPage(1)
print('rotating page')
page.rotateClockwise(90) #angles can only be multiples of 90
#rotateCounterClockwise
writer.addPage(page)

#we can use loop to rotate multiple pages

output=open('D:\\py\\Extraction_pdf\\newfile.pdf','wb')
#wb for writing/overwriting
writer.write(output)  #to write the data in output
print('rotated and saved')

output.close()
input.close()