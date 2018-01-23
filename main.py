import file_reader

# DOCX Correct File
print(file_reader.read_file('/Users/Mohnish_Devadiga/Desktop/Data/resume.docx'))
#DOCX Error File
print(file_reader.read_docx('/Users/Mohnish_Devadiga/Desktop/Data/Error-Project-Status-Report.docx'))
#PDF Correct
print(file_reader.read_file('/Users/Mohnish_Devadiga/Desktop/Data/resume.pdf'))