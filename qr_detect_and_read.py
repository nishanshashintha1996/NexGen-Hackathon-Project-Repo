import picamera
from time import sleep

import pyqrcode

print("About to take a picture ")
with picamera.PiCamera() as camera:
	camera.resolution = (1280,720)
	sleep(3)
	camera.capture("qr.jpg")
print("picture taken")


from pyzbar.pyzbar import decode
from PIL import Image
d = decode(Image.open('qr.jpg'))
print(d[0].data.decode('ascii'))
