# import qrcode as qr
# img= qr.make("https://www.linkedin.com/in/ravi-raushan13/")
# img.save("linkedin_Ravi.png")
import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=15,border=4,)
qr.add_data("https://www.linkedin.com/in/ravi-raushan13/")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="Black")
img.save("linkedin_qr_ravi.png")
