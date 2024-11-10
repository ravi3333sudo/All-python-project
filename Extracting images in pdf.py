# pip install pikepdf

from pikepdf import Pdf, Name , PdfImage

old_pdf =Pdf.open("css.pdf")
page_1=old_pdf.pages[0]
#print(list(page_1.images.key())) ['/Image13','/image5']

raw_image = page_1.images['/Image13']
pdf_image = PdfImage(raw_image)
pdf_image.extract_to(fileprefix="extract1")