import PyPDF2, os
os.chdir('.\\13. pdf')

pdfFileObj = open('Recursion_Chapter1.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pdfWriter = PyPDF2.PdfWriter()                                          # lets you create a new pdf object

for pageNum in range(len(pdfReader.pages)):
    pageOjb = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageOjb)

for pageNum in range(len(pdfReader.pages)):
    pageOjb = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageOjb)


pdfOutputFile = open('combinedpdf.pdf', 'wb')
pdfWriter.write(pdfOutputFile)                              # creates new pdf file 
pdfOutputFile.close()
pdfFileObj.close()
