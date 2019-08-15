import pyqrcode
from PIL import Image
#import png
url = pyqrcode.QRCode('raj goyal',error = 'H')
url.png('test.png',scale=10)
im = Image.open('test.png')
im = im.convert("RGBA")
logo = Image.open('bookmypgcropped.jpg')
box = (140,180,260,240)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.show()
im.save('raj1.png')
