import numpy as np

def translate(m,n=0):
    return np.array([[1,0,m],
                     [0,1,n],
                     [0,0,1]])

def rotate(ang):
    return np.array([[np.cos(ang),-np.sin(ang),0],
                     [np.sin(ang),np.cos(ang),0],
                     [0,0,1]])

def getEndPos(X):
    return X[0,2], X[1,2]

def getAng(X):
    return np.arctan2(X[1,0],X[0,0])

def main():
    joints = int(input('How many joints? '))
    t = np.eye(3, dtype=float)
    for i in range(joints):
        ang = float(input('Angle in radians? '))
        l   = int(input('Length of link? '))
        t = t.dot(rotate(ang)).dot(translate(l))
    endX, endY = getEndPos(t)
    print('The end of the arm is at ('+
            str(endX)+', '+str(endY)+')')
    print('The angle from the X-axis is '+str(getAng(t))+
            ' radians')

if __name__ == '__main__':
    main()
