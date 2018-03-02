import cv2
import numpy as np
import math

class TargetFinder ():
	def __init__ (self):
		print('TargetFinder init')

		self.hsvGreenBoundaries = ((40, 60, 60), (80, 255, 255))
		self.hsvRedBoundaries = ((0, 150, 60), (18, 255, 255))
		self.hsvBlueBoundaries = ((90, 180, 180), (131, 255, 255))

		self.redBoundaries = ((22, 17, 181), (62, 67, 255))
		self.blueBoundaries = ((180, 30, 30), (255, 215, 160))
		self.greenBoundaries = ((80, 170, 160), (140, 255, 210))

	def processShape (self, contour):
		peri = cv2.arcLength(contour, True)
		approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
		return len(approx) == 4

	def processFrame (self, frame, boundaries):
		(lower, upper) = boundaries
		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")

		frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		blurred = cv2.GaussianBlur(frame_hsv, (5, 5), 0)

		mask = cv2.inRange(blurred, lower, upper)
		kernel = np.ones((2,2),np.uint8)

		erosion = cv2.erode(mask, kernel, iterations=4)
		dilation = cv2.dilate(erosion, kernel, iterations=4)

		edged = cv2.Canny(dilation, 50, 150)

		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
		# cnts = list(filter(lambda cnt: self.processShape(cnt), cnts))
		# center = None

		# loop over the contours

		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			
			try:
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			except:
				pass
	 
			# only proceed if the radius meets a minimum size
			if radius > 20:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
				
		return frame

	def findColor (self, frame, boundaries):
		# (lower, upper) = ((0, 0, 0), (15, 15, 15))
		(lower, upper) = boundaries

		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")

		frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		blurred = cv2.GaussianBlur(frame_hsv, (5, 5), 0)

		mask = cv2.inRange(blurred, lower, upper)
		kernel = np.ones((2,2), np.uint8)

		erosion = cv2.erode(mask, kernel, iterations=4)
		dilation = cv2.dilate(erosion, kernel, iterations=4)

		(left, right) = self._split_in_two(dilation)

		left_count = left.sum().sum()
		right_count = right.sum().sum()

		if not left_count and not right_count:
			return 0
		else:
			return 'left' if left_count > right_count else 'right'



	def _split_in_two (self, arr):
		half = math.ceil(arr.shape[1] / 2)
		return np.split(arr, [half], 1)

		# cv2.imshow('img', mask)
