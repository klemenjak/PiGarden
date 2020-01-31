from os import chdir
from time import sleep
from picamera import PiCamera
from datetime import datetime

from dpbox_handler import *

camera = PiCamera()
camera.resolution = (2592, 1944)

dbox = init_dropbox()

while True:
	camera.start_preview()
	sleep(60)

	now = datetime.now()
	annotation = now.strftime("%m-%d_%H:%M")
	camera.annotate_text = annotation
	image_file = '../pics/plants/{}.jpg'.format(annotation)

	camera.capture(image_file)
	camera.stop_preview()

	chdir('../pics/plants/')
	upload_file(dbox, '{}.jpg'.format(annotation), '/PiGarden/')
	chdir('../PiGarden/')
