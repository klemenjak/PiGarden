from os import chdir
from time import sleep, ctime
from picamera import PiCamera
from datetime import datetime

from dpbox_handler import *

camera = PiCamera()
camera.resolution = (2592, 1944)

dbox = init_dropbox()

while True:
	camera.start_preview()
	now = datetime.now()
	camera.annotate_text = ctime()

	annotation = now.strftime("%m-%d_%H:%M")
	image_file = '../pics/plants/{}.jpg'.format(annotation)

	camera.capture(image_file)
	camera.stop_preview()

	chdir('../pics/plants/')

	try:
		upload_file(dbox, '{}.jpg'.format(annotation), '/PiGarden/')
	except ConnectionError:
		pass

	chdir('../../PiGarden/')
	sleep(3600)
