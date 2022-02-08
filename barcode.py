import pyqrcode as qr
import cv2 as cv
from pyzbar.pyzbar import decode

##barcode making
url=qr.create('Test Barcode')
#saving as svg
url.svg('test.svg', scale=8)
print(url.terminal(quiet_zone=1))
#saving as png
url.png('test.png',8)

barkod=cv.imread('test.png')
cv.imshow('barkod',barkod)
cv.waitKey(0)

#decoding qrcode
for coder in decode(barkod):
    print(coder.data.decode('utf-8'),coder.type)
