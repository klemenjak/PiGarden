from picamera import PiCamera
from datetime import datetime

from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)

for i in range(10):
	camera.start_preview()
	camera.annotate_text = "Hellas!"
	sleep(5)
	now = datetime.now()
	camera.capture('pics/plants/%s.jpg' % now.strftime("%Y-%m-%d_%H:%M:%S"))
	camera.stop_preview()
	
