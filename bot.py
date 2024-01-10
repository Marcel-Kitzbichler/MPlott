import event, time, cyberpi, mbuild, mbot2
import time

imgBuffer =[
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,True,False,False,False,True,True,False],
    [False,True,True,False,False,False,True,True,False],
    [False,True,False,True,False,True,False,True,False],
    [False,True,False,True,False,True,False,True,False],
    [False,True,False,False,True,False,False,True,False],
    [False,True,False,False,True,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False],
    [False,True,False,False,False,False,False,True,False]
]
currLine = []


def forward():
    mbot2.EM_reset_angle("EM1")
    mbot2.servo_set(95,"all")
    cyberpi.broadcast("handleServo")
    mbot2.straight(10,20)
    cyberpi.stop_other()
    mbot2.servo_set(95,"all")


def back():
    mbot2.turn(3)
    mbot2.straight(-10,20)
    mbot2.turn(-3)

def drawLine():
    forward()
    back()

def drwImg():
    global currLine
    for i in imgBuffer:
        currLine = i
        drawLine()


@event.is_press('a')
def main():
    time.sleep(2)
    drwImg()

@event.receive("handleServo")
def servoHandler():
    while True:
        pixel = int(mbot2.EM_get_angle("EM1")/17)
        if pixel > len(currLine)-1:
            mbot2.servo_set(95,"all")
            cyberpi.stop_this()
        i = currLine[pixel]
        if i:
            mbot2.servo_set(88.4,"all")
        else:
            mbot2.servo_set(95,"all")