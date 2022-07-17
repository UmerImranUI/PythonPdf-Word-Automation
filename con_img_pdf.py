import img2pdf

img="unsplash.jpg"

f=open('outpdf.pdf', 'wb')
f.write(img2pdf.convert(img))
f.close()