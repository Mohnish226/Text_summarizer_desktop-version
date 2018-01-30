import file_reader
import termFreq
import wiki_read


# DOCX Correct File
print(file_reader.read_file('/Users/Mohnish_Devadiga/Desktop/Data/resume.docx'))
#DOCX Error File
print(file_reader.read_docx('/Users/Mohnish_Devadiga/Desktop/Data/Error-Project-Status-Report.docx'))
#PDF Correct
print(file_reader.read_file('/Users/Mohnish_Devadiga/Desktop/Data/resume.pdf'))

#termFreq.run_tfidf()

wiki_read.topic("Automatic_summarization")
url = "https://en.wikipedia.org/wiki/Battle_of_Plassey"
if "wikipedia.org/wiki" in url:
    wiki_read.link(url)
else:
    print("Topic name")