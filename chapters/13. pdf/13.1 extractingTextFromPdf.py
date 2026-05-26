# to work with pdf we need the PyPDF2 pkg
# pip install PyPDF2

import PyPDF2, os
os.chdir('.\\13. pdf')

pdfFileObj = open('Recursion_Chapter1.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

print('Total pages of the pdf: ', str(len(pdfReader.pages)))

pageObj = pdfReader.pages[0]
# print(pageObj.extract_text())         # extracts text of all page

print('is pdf encrypted: ', str(pdfReader.is_encrypted))                # this checks weather the file hass a password or not

# if the file has the password then we can decrypt the file like
# pdfReader.decrypt('password')

# to encrypt the pdf we use:
# pdfWriter obj     -> you will understand in 13.3 how to create writer obj
# pdfwriter.encrypt('password')

