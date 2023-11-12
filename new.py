import qrcode
from PIL import Image


link=input("Enter LINK / TEXT for generator Qr code : ")

# ایجاد شیء QRCode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=50, border=2)
qr.add_data(link)
qr.make(fit=True)

# ایجاد تصویر کد QR
img_qr = qr.make_image(fill='black', back_color='white')
name=input('file name : ')
# ذخیره کد QR به فایل تصویری
img_qr.save(f'{name}.png')

