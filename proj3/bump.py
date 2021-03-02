import rospy
import time
from turtleAPI import robot

rob = robot()

r = rospy.Rate(10)

rob.drive(linSpeed=.3)

while not rospy.is_shutdown():
    status = rob.getBumpStatus()
    if status['state']==1:
        print(status)
        rob.stop()
        direction = .5
        wait = 2
        if status['bumper']==0:
            direction = -.5
        if status['bumper']==1:
            wait = 5
        rob.drive(linSpeed=-.2)
        time.sleep(1)
        rob.drive(angSpeed=direction)
        time.sleep(wait)
        rob.drive(linSpeed=.3)
    r.sleep()

rob.stop()
