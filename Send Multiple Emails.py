import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('#put gmail','#password')
subject="test python"
body="i love python"
message="subject:{}\n\n{}".format(subject,body)
listadd=['1st mail','2mail','3rd mail']
ob.sendmail('#put gmail',listadd,message)
print("Send mail")
ob.quit()
