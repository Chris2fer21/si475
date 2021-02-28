import turtleAPI as turt
import Queue as queue
import math, rospy

rob = turt.robot()

ang_error_queue = queue.Queue()
ang_error_sum = 0
prev_ang_error = 0

def angle_pid(robot, goalX, goalY):
    global ang_error_queue, ang_error_sum, prev_ang_error
    
    pos = robot.getPositionTup()
    x = pos[0]
    y = pos[1]
    yaw = pos[2]
    dist_to_goal = distance(x, y, goalX, goalY)
    ang_to_goal = math.atan2((goalY-y)/dist_to_goal, (goalX-x)/dist_to_goal)
    print("angle to goal " + str(ang_to_goal))
    print("yaw " + str(yaw))
    ang_error = ang_to_goal - yaw
    print("error " + str(ang_error))
    kp = 0.2
    ki = 0.01
    kd = 0
    
    #update integral for last five steps
    if ang_error_queue.empty() == False and ang_error_queue.qsize() == 5:
        ang_error_sum -= ang_error_queue.get()
    ang_error_queue.put(ang_error)
    ang_error_sum += ang_error

    #update derivative
    ang_error_deriv = ang_error - prev_ang_error

    ut = kp * ang_error + ki * ang_error_sum + kd * ang_error_deriv

    prev_ang_error = ang_error

    return ut

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

goalX = int(input("Goal X: "))
goalY = int(input("Goal Y: "))

pos = rob.getPositionTup()
ang_speed = 0
r = rospy.Rate(1)
while distance(goalX, goalY, pos[0], pos[1]) > 0.1 and not rospy.is_shutdown():
    ut = angle_pid(rob, goalX, goalY)
    print("ut " + str(ut))
    print()
    ang_speed = ut
    rob.drive(ang_speed, 0.1)
    pos = rob.getPositionTup()
    r.sleep()

rob.stop()
