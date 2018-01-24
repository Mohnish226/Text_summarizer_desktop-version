# -*- coding: utf-8 -*-
"""
Copmbined with file_reader
"""

from docx import Document

document=Document("C:/Users/ADMIN/Downloads/question bank first test.docx")
fullText = ""
for para in document.paragraphs:
        fullText+=(para.text)
print(fullText)