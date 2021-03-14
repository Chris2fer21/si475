import numpy as np
import rospy
import time
from turtleAPI import robot

rob = robot()

r = rospy.Rate(10)

rob.drive(linSpeed=.3)

while not rospy.is_shutdown():
    depth = rob.getDepth()
    rows, cols = depth.shape
    depth = depth[(rows/2):,:]
    #print(depth.shape)
    left = depth[:,:(cols/3)]
    midd = depth[:,(cols/3):(2*cols/3)]
    righ = depth[:,(2*cols/3):]
    #print(left.shape)
    #print(midd.shape)
    #print(righ.shape)
    midd = midd[np.logical_not(np.isnan(midd))]
    left = left[np.logical_not(np.isnan(left))]
    righ = righ[np.logical_not(np.isnan(righ))]
    midd = np.average(midd)
    righ = np.average(righ)
    left = np.average(left)
    if midd>.5:
        midd = .5
    rob.drive(linSpeed=midd,angSpeed=(left-righ))
    """
    #print(midd.shape)
    if midd<1:
        #print(status)
        rob.stop()
        direction = .5
        wait = 2
        if left < righ:
            direction = -.5
        rob.drive(linSpeed=-.2)
        time.sleep(1)
        rob.drive(angSpeed=direction)
        time.sleep(wait)
        rob.drive(linSpeed=.3)"""
    r.sleep()

rob.stop()
