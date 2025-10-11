
#1
import qrcode

data = 'this is a test'

img = qrcode.make(data)

img.save('qrcode.png')
#######

#2
import qrcode

data = 'this is a test'

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image()
img.save('qrcode.png')

#3 Decoder
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('qrcode.png')
result = decode(img)

print(result)

