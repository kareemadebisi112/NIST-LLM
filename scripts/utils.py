import PyPDF2

def extractPDF(path):
    pdfFile = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)

    text = ""
    for page in range(len(pdfReader.pages)):
        pageObj = pdfReader.pages[page]
        text += pageObj.extract_text()

    print(text[124])
