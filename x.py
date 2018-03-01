import cv2
from utils.TargetFinder import TargetFinder

finder = TargetFinder()
camera = cv2.VideoCapture(0)

# img = cv2.imread('not_eguz.jpg')
# processed = finder.findColor(img, finder.hsvBlueBoundaries)

# cv2.imshow('hue', processed)
# key = cv2.waitKey(0)

while True:
	(grabbed, frame) = camera.read()
	# frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	frame = finder.findColor(frame, finder.hsvBlueBoundaries)
	print(frame)
	# cv2.imshow('img', frame)
	key = cv2.waitKey(1) & 0xFF