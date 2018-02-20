import cv2
import numpy as np
from utils import TargetFinder

from cscore import CameraServer
from networktables.util import ntproperty


def main ():
	class Table ():
		target = ntproperty('/target', 0)
		def __init__ (self):
			pass

	networkTable = Table()
	cs = CameraServer.getInstance()
	cs.enableLogging()
	
	camera = cs.startAutomaticCapture()
	
	camera.setResolution(320, 240)
	
	# Get a CvSink. This will capture images from the camera
	cvSink = cs.getVideo()
	
	# (optional) Setup a CvSource. This will send images back to the Dashboard
	outputStream = cs.putVideo("Ultra cool vision", 320, 240)
	
	# Allocating new images is very expensive, always try to preallocate
	img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)    

	finder = TargetFinder.TargetFinder()

	while True:
		# Tell the CvSink to grab a frame from the camera and put it
		# in the source image.  If there is an error notify the output.
		time, img = cvSink.grabFrame(img)
		if time == 0:
			# Send the output the error.
			outputStream.notifyError(cvSink.getError());
			# skip the rest of the current iteration
			continue
		
		# Process frame
		img = finder.processFrame(img, finder.hsvBlueBoundaries)
		direction = finder.findColor(img, finder.hsvBlueBoundaries)
		# sd.putValue('autoDirection', direction)
		networkTable.target = direction

		# Give the output stream a new image to display
		outputStream.putFrame(img)