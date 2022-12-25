from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import io
#------------------ pip installs
#pip install pdf
#pip install PyPDF2
#pip install PyPDF4
#------------------ metadata
pdf_path = r"C:\\Users\\path\\Git Terminology 101.pdf"
with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        print(information)
        print(number_of_pages)


#------------------ extract text
pdf_obj = open(pdf_path, 'rb')
pdf_reader = PdfFileReader(pdf_obj) # pdf reader object
text= ''
for i in range(0,pdf_reader.numPages):
    # creating a page object
    page_obj = pdf_reader.getPage(i)
    # extracting text from page
    text = text + page_obj.extractText()
print(text)

