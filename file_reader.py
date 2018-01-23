#import docx
import PyPDF2 as pypdf
import docx2txt



def read_docx(file_name):
    '''
    :param file_name:
    :return:
    '''
    """
    document = docx(file_name)
    text = ""
    for para in document.paragraphs:
        text += (para.text)
    return(text)
    """
    return(docx2txt.process(file_name))

def read_pdf(file_name):
    file = pypdf.PdfFileReader(file_name)
    text = ""
    pages = file.getNumPages()
    for x in range(0, pages):
        page = file.getPage(x)
        text += page.extractText()
    return(text)

def read_file(file_name):
    print(file_name.split(".")[-1])