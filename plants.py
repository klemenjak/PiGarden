from time import sleep
from picamera import PiCamera
from datetime import datetime

from dpbox_handler import *

camera = PiCamera()
camera.resolution = (2592, 1944)

dbox = init_dropbox()

while True:
	camera.start_preview()
	sleep(5)
	now = datetime.now()
	annotation = now.strftime("%Y-%m-%d_%H:%M:%S")
	camera.annotate_text = annotation
	image_file = '../pics/plants/{}.jpg'.format(annotation)
	camera.capture(image_file)
	camera.stop_preview()
	upload_file(dbox, image_file, '/PiGarden/')
