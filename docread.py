# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 00:13:48 2018

@author: ADMIN
"""

from docx import Document

document=Document("C:/Users/ADMIN/Downloads/question bank first test.docx")
fullText = ""
for para in document.paragraphs:
        fullText+=(para.text)
print(fullText)