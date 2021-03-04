from turtleAPI import robot
import cv2

r = robot()

img = r.getImage()
cv2.imshow("green",img)
x = cv2.waitKey(90000)
