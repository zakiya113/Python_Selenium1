import PyPDF2
newfile = open('hello.txt','w')
file = open('C:\\Users\\minds9\\PycharmProjects\\Python_Selenium\\TestPDF\\Sample.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
pageobj = pdfreader.getPage(0)
print(pageobj.extractText())
file.close()
newfile.close()