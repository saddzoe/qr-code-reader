# qr-code-reader
# This is a simple program that makes a qr code reader which takes you to a python tutorial

import pyqrcode
from qyqrcode import QRCode

# This represents the QR code
q = "https://www.youtube.com/watch?v=rfscVS0vtbw"

# This would generate the QR Code
url = pyqrcode.create(q)

url.svg("myyoutube.svg", scale=15)

