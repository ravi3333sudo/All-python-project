# pip install pikepdf

import pikepdf

old_pdf = pikepdf.Pdf.open("css.pdf")

for n,page_can in enumerate(old_pdf.pages):
    new_pdf = pikepdf.Pdf.new()
    new_pdf.pages.append(page_can)
    name ="test"+str(n)+".pdf"
    new_pdf.save(name)