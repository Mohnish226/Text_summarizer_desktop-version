# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:41:14 2018

@author: ADMIN
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


