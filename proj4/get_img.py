from turtleAPI import robot
import cv2
import rospy
import matplotlib as plt
import numpy as np
import math

def findCoM(light, dark, img):

    hsv_test = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

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


    if (num!=0):
        x = sum/num

    if not (math.isnan(x)):
        for row in range(len(mask)):
            mask[row,int(x)] = 0

    print(x)

    cv2.imwrite("mask.jpg", mask)

    return x

color = raw_input("Color? ")

if color == 'green':
    light = (40,15,20)
    dark = (80,255,235)

if color == 'purple':
    light = (140,15,20)
    dark = (165,255,235)

if color == 'red':
    light = (0,15,20)
    dark = (7,255,235)

if color == 'yellow':
    light = (25,15,20)
    dark = (40,255,235)

if color == 'blue':
    light = (110,15,80)
    dark = (135,255,190)

r = robot()


img_rgb = r.getImage()
cv2.imwrite('test.jpg',img_rgb)
img_hsv = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2HSV)
cv2.imwrite('before.jpg',img_hsv)
outhsv = cv2.inRange(img_hsv,light,dark)
cv2.imwrite('after.jpg',outhsv)

def get_ang_err(com, P=.5):
    return P*(320-com)

def get_dist_err(dens,P=.5):
    return P*(921600-dens)

ros = rospy.Rate(10)

while not rospy.is_shutdown():
    img = r.getImage()
    err = 320-findCoM(light,dark,img)
    if err > .2:
        err = .2
    if err < -.2:
        err = -.2
    if err==0:
        r.drive(angSpeed=2,linSpeed=0)
    else:
        r.drive(angSpeed=err,linSpeed=.1)
    ros.sleep()

