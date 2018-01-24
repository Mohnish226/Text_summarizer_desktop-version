# -*- coding: utf-8 -*-
"""
Copmbined with file_reader
"""

import PyPDF2 as pypdf



def read_pdf(file_name):
    file = pypdf.PdfFileReader(file_name)
    text = ""
    pages = file.getNumPages()
    for x in range(0, pages):
        page = file.getPage(x)
        text += page.extractText()
    return(text)


