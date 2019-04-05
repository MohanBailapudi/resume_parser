import PyPDF2
import requests

# PDFfilename = "KORADAVENKATASHRIRAMGUPTA.pdf" #filename of your PDF/directory where your PDF is stored
#
# pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb")) #PdfFileReader object
#
# pg1 = pfr.getPage(1) #extract pg 4
# # pg8 = pfr.getPage(7) #extract pg 8
#
# writer = PyPDF2.PdfFileWriter() #create PdfFileWriter object
# #add pages
# writer.addPage(pg1)
# # writer.addPage(pg8)
#
#
# NewPDFfilename = "allTables.pdf" #filename of your PDF/directory where you want your new PDF to be
# with open(NewPDFfilename, "wb") as outputStream: #create new PDF
#     writer.write(outputStream) #write pages to new PDF


# from tabula import read_pdf
#
# df = read_pdf("RaghavendraLade.pdf")
#
# print(df)

# def pdfToTable(PDFfilename, apiKey, fileExt, downloadDir):
#     fileData = (PDFfilename, open(PDFfilename, 'rb'))
#     files = {'f': fileData}
#     postUrl = "https://pdftables.com/api?key={0}&format={1}".format(apiKey, fileExt)
#     response = requests.post(postUrl, files=files)
#     response.raise_for_status()
#     with open(downloadDir, "wb") as f:
#         f.write(response.content)
#
#
#
#
# pdfToTable('allTables.pdf','dJFkAgBX38Gf7NXg', 'csv', 'example.csv')


# from docx import Document
#
# wordDoc = Document('ADISEKHARREDDYMEDAPATI.docx')
#
# for table in wordDoc.tables:
#     rows =table.rows
#     header = []
#     for cell in rows[0].cells:
#         header.append(cell.text)
#     for row in rows[1:]:
#         i = 0
#         for cell in row.cells:
#             print(header[i],cell.text)
#             i = i+1


from keras_en_parser_and_analyzer.library.utility.pdf_utils import pdf_to_text, convert_pdf_to_txt, convert_pdf_to_html

print(convert_pdf_to_html("RaghavendraLade.pdf"))