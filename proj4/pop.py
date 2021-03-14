from turtleAPI import robot
import cv2
import numpy as np
 
def findCoM(light, dark, img):
	
	hsv_test = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

	mask = cv2.inRange(hsv_test, light, dark)	

	array = np.zeros(len(mask[0]))
	num = 0

	for col in range(len(mask[0])):
		for row in range(len(mask)):
			array[col] += mask[row,col]
			num += mask[row,col]

	sum = 0
	i = 0
	for x in array:
		sum += x*i
		i +=1


	x = sum/num

	for row in range(len(mask)):
		mask[row,int(x)] = 0

	print(x)

	cv2.imwrite("mask.jpg", mask)

	return x



bot =robot()

test = bot.getImage()

cv2.imwrite("org.jpg", test)
#cv2.waitKey(0)
print test[10,10]

stuff, junk = cv2.threshold(test, 100, 255, cv2.THRESH_BINARY)
cv2.imwrite("test.jpg", junk)

lightGreen = np.array([35, 15, 20])
darkGreen = np.array([80, 255, 255])

#hsv_test = cv2.cvtColor(test, cv2.COLOR_RGB2HSV)

#mask = cv2.inRange(hsv_test, lightGreen, darkGreen)

#print mask[100,100]

findCoM(lightGreen, darkGreen, test)

def findCoM(light, dark, img):
	
	hsv_test = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

	mask = cv2.inRange(hsv_test, light, dark)	

	array = np.zeros(len(mask[0]))
	num = 0

	for col in range(len(mask[0])):
		for row in range(len(mask)):
			array[col] += mask[row,col]
			num += mask[row,col]

	sum = 0
	i = 0
	for x in array:
		sum += x*i
		i +=1


	x = sum/num

	for row in range(len(mask)):
		mask[row,int(x)] = 0

	print(x)

	cv2.imwrite("mask.jpg", mask)

	return x

