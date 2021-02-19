#BROPHY AND HARTLEY FORWARD KINEMATICS PROJECT
from arm_controller import ArmController
import numpy as np

def rotateZ(theta):
    rot = np.array(
            [[np.cos(theta), -(np.sin(theta)), 0, 0],
                [np.sin(theta), np.cos(theta), 0, 0],
		[0,0,1,0],
                [0,0,0,1]]
            )

    return rot

def rotateX(theta):
    rot = np.array(
            [[1,0,0,0],
		[0, np.cos(theta), -(np.sin(theta)), 0],
                [0, np.sin(theta), np.cos(theta), 0],
                [0,0,0,1]]
            )

    return rot


def trans(x,y,z):

    tran = np.array(
            [
                [1,0,0,x],
                [0,1,0,y],
		[0,0,1,z],
                [0,0,0,1]
            ])

    return tran

phi1 = input('Enter angle 1:')
phi2 = input('Enter angle 2:')
phi3 = input('Enter angle 3:')
phi4 = input('Enter angle 4:')

#first joint
t = trans(.012,0,0)
t = np.dot(t, rotateZ(phi1))
t = np.dot(t, trans(0,0,.077))
t = np.dot(t, rotateX(1.57))
#second joint
t = np.dot(t, rotateZ((np.pi/2 - np.sin(.024/.13)) - phi2))
t = np.dot(t, trans(.13,0,0))

#third joint
t = np.dot(t, rotateZ(-phi3 - (np.pi/2 - np.sin(.024/.13))))
t = np.dot(t, trans(.124,0,0))

#fourth joint
t = np.dot(t, rotateZ(-phi4))
t = np.dot(t, trans(.126,0,0))

#normalize to reference frame
t = np.dot(t, rotateX(-np.pi/2))

#calculate yaw,pitch,roll
pitch = np.arctan2(-t[2,0], np.sqrt(np.square(t[0,0]) + np.square(t[1,0])))
yaw = np.arctan2((t[1,0]/np.cos(pitch)), (t[0,0]/np.cos(pitch)))
roll = np.arctan2((t[2,1]/np.cos(pitch)), (t[2,2]/np.cos(pitch)))

ac=ArmController()
ac.set_joints([phi1,phi2,phi3,phi4])
print('The end of the arm is at (' + t[0,3].astype(str) + ', ' + t[1,3].astype(str) + ', ' + t[2,3].astype(str) + ')')
print('The orientation is (' + roll.astype(str) + ', ' + pitch.astype(str) + ', ' + yaw.astype(str) + ')')
print('***From ArmController for Verification***')
print(ac.get_pose())
