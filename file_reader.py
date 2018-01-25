'''
To Read Microsoft Documents or PDF's
'''
import PyPDF2 as pypdf
from docx import Document


def read_docx(file_name):
    try:
        document = Document(file_name)
        text = ""
        for para in document.paragraphs:
            text += para.text
            print(para.text)
        return(1)
    except:
        return(0)


def read_pdf(file_name):
    try:
        file = pypdf.PdfFileReader(file_name)
        text = ""
        pages = file.getNumPages()
        for x in range(0, pages):
            page = file.getPage(x)
            text += page.extractText()
        print(text)
        return(1)
    except:
        return(0)


def read_file(file_name):
    file_ext = file_name.split(".")[-1]
    if file_ext == "docx" or file_ext == "DOCX":
        if read_docx(file_name) == 1:
            return(1)
        else:
            return(0)
    if file_ext == "PDF" or file_ext == "pdf":
        if read_pdf(file_name) == 1:
            return(1)
        else:
            return(0)