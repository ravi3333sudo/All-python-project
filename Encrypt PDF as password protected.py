import pikepdf

old_pdf = pikepdf.Pdf.open("css.pdf")

no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("pro_new.pdf",encryption= pikepdf.Encryption(user="123ravi",owner="ravirazz",allow=no_extr))