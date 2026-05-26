import PyPDF2, os
os.chdir('.\\13. pdf')

pdfFileObj = open('Recursion_Chapter1.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
page = pdfReader.pages[0]
page.rotate(90)

pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)

rotatedpdf = open('rotatedpdf.pdf', 'wb')
pdfWriter.write(rotatedpdf)

rotatedpdf.close()
pdfFileObj.close()