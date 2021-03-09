from turtleAPI import robot
import cv2
import rospy

r = robot()

T = 0
while not rospy.is_shutdown:
    img = r.getImage()
    cv2.imshow("green",img)
    cv2.waitKey(1)
    T = img

for i in range(230,250):
    for j in range(310,330):
        print(T[i][j])

def get_ang_err(com, P=.5):
    return P*(320-com)

def get_dist_err(dens,P=.5):
    return P*(921600-dens)

print(img.shape)
