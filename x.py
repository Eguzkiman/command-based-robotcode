import cv2
from utils.TargetFinder import TargetFinder

finder = TargetFinder()
camera = cv2.VideoCapture(0)

while True:
	(grabbed, frame) = camera.read()
	print(finder.findColor(frame, finder.greenBoundaries))