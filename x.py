import cv2
from utils.TargetFinder import TargetFinder

finder = TargetFinder()
camera = cv2.VideoCapture(0)

while True:
	(grabbed, frame) = camera.read()
	# frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	print(frame)
	frame = finder.processFrame(frame, finder.hsvRedBoundaries)
	cv2.imshow('img', frame)
	key = cv2.waitKey(1) & 0xFF