import event, time, cyberpi, mbuild, mbot2
import time
#--------------------Settings-----------------------
stepsPerPixel = 12
pixelHeight = 4
rowLength = 8
forwardSpeed = 10
backwardSpeed = 10
backAngle = 3
upPos = 95
downPos = 88.4
#---------------------------------------------------

imgBuffer =[
    [False,True,False,False,False,False,False,True,False],
    [False,True,True,False,False,False,True,True,False],
    [False,True,False,True,False,True,False,True,False],
    [False,True,False,False,True,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False]
]
currLine = []


def forward():
    mbot2.EM_reset_angle("EM1")
    mbot2.servo_set(upPos,"S1")
    cyberpi.broadcast("handleServo")
    mbot2.straight(rowLength,forwardSpeed)
    cyberpi.stop_other()
    mbot2.servo_set(upPos,"S1")


def back():
    mbot2.turn(backAngle)
    mbot2.straight(rowLength*-1,backwardSpeed)
    mbot2.turn(backAngle*-1)

def drawLine():
    forward()
    back()

def drwImg():
    global currLine
    for i in imgBuffer:
        currLine = i
        for a in range(pixelHeight):
            drawLine()


@event.is_press('a')
def main():
    time.sleep(2)
    drwImg()

@event.receive("handleServo")
def servoHandler():
    while True:
        pixel = int(mbot2.EM_get_angle("EM1")/stepsPerPixel)
        if pixel > len(currLine)-1:
            mbot2.servo_set(upPos,"1")
            cyberpi.stop_this()
        i = currLine[pixel]
        if i:
            mbot2.servo_set(downPos,"S1")
        else:
            mbot2.servo_set(upPos,"S1")