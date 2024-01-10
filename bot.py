import event, time, cyberpi, mbuild, mbot2
import time

imgBuffer =[
    [True],
    [False,True],
    [False,False,True],
    [False,False,False,True],
    [False,False,False,False,True],
    [False,False,False,False,False,True],
    [False,False,False,False,False,False,True],
    [False,False,False,False,False,False,False,True],
    [False,False,False,False,False,False,False,False,True],
    [False,False,False,False,False,False,False,False,False,True]
]
currLine = []


def forward():
    mbot2.servo_set(95,"all")
    cyberpi.broadcast("handleServo")
    mbot2.straight(10,10)
    cyberpi.stop_other()
    mbot2.servo_set(95,"all")


def back():
    mbot2.turn(3)
    mbot2.straight(-10)
    mbot2.turn(-3)

def drawLine():
    forward()
    back()

def drwImg():
    global currLine
    for i in imgBuffer:
        currLine = i
        drawLine()


@event.start
def main():
    drwImg()

@event.receive("handleServo")
def servoHandler():
    for i in currLine:
        if i:
            mbot2.servo_set(88.4,"all")
        else:
            mbot2.servo_set(95,"all")
        time.sleep(0.2)
    mbot2.servo_set(95,"all")