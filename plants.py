from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.resolution = (2592, 1944)

while True:
	camera.start_preview()
	sleep(5)
	now = datetime.now()
	annotation = now.strftime("%Y-%m-%d_%H:%M:%S")
	camera.annotate_text = annotation
	camera.capture('../pics/plants/{}.jpg'.format(annotation))
	camera.stop_preview()
