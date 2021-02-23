import turtleAPI as turt

R = turt.robot()

#R.drive(linSpeed=.5)

while (true):
    print(R.getBumpStatus())
