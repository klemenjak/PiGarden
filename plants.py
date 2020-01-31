from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)

for i in range(10):
	camera.start_preview()
	camera.annotate_text = "Hellas!"
	sleep(5)
	camera.capture('pics/plants/image%s.jpg' % i)
	camera.stop_preview()


