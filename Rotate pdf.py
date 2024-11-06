import pikepdf

old_my =pikepdf.Pdf.open("css.pdf")
# print(pdf_my.pages)
for i in old_my.pages:
    i.Rotate = 180
    old_my.save("new_pdf.pdf")