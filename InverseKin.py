from arm_controller import ArmController
import numpy as np

#get inputs from user
x = input('Enter X:')
y = input('Enter Y:')
z = input('Enter Z:')
roll = input('Enter Roll:')
pitch = input('Enter Pitch:')
yaw = input('Enter Yaw:')

#putinputs into the final matrix
t = [[np.cos(yaw)*np.cos(roll), -np.sin(yaw)*np.cos(pitch) + np.cos(yaw)*np.sin(roll)*np.sin(pitch), 
      np.sin(yaw)*np.sin(pitch)+np.cos(yaw)*np.sin(roll)*np.cos(pitch), x],
        [np.sin(yaw)*np.cos(roll), np.cos(yaw)*np.cos(pitch) + np.sin(yaw)*np.sin(roll)*np.sin(pitch), 
         -np.cos(yaw)*np.sin(pitch) + np.sin(yaw)*np.sin(roll)*np.cos(pitch), y],
        [-np.sin(roll), np.cos(roll)*np.sin(pitch), np.cos(roll)*np.cos(pitch), z],
        [0, 0, 0, 1]]



#first joint
phi1 = np.arctan2(-t[0][1], t[1][1])
#calculate cos2 and sin2
cos2 = (t[0][3] - t[1][1]*.126*t[2][2])/(.19567*t[1][1])
sin2 = (t[2][3] - .126*t[2][0]-.077)/.19567
phi2 = np.arctan2(sin2, cos2)-.8577
phi4 = np.arctan2(t[2][0], t[2][2]) - np.arctan2(sin2, cos2) + .8577

s = [[np.cos(.1)*np.cos(.1+.1), -np.sin(.1), -np.cos(.1)*np.sin(.2), .126*np.cos(.1)*np.cos(.2) + np.cos(.1)*.19567*np.cos(.1+.71306)],
     [np.sin(.1)*np.cos(.2), np.cos(.1), -np.sin(.1)*np.sin(.2), .126*np.sin(.1)*np.cos(.2) + np.sin(.1)*.19567*np.cos(.1+.71306)],
     [np.sin(.2), 0, np.cos(.2), .126*np.sin(.2)+.19567*np.sin(.1+.71306)+.077],
     [0,0,0,1]]

#print(t)
#print('//////////////')
#print(s)

#print joints
print('The joint values needed are: ' + phi1.astype(str) + ' ' +phi2.astype(str)+ ' ' +phi4.astype(str))

ac=ArmController()
ac.set_joints([phi1,-phi2,0,-phi4])
print('***From ArmController for Verification***')
print(ac.get_pose())
