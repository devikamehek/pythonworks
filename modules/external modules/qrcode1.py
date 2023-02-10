import pyqrcode
from pyqrcode import QRCode

s="Hello World"
url=pyqrcode.create(s)
url.svg("qrcode1.svg",scale=8)



