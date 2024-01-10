import event, time, cyberpi, mbuild, mbot2
import time


def forward():
    mbot2.servo_set(91,"all")
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


@event.start
def main():
    mbot2.servo_set(95,"all")
    time.sleep(1)
    while True:
        drawLine()

@event.receive("handleServo")
def servoHandler():
    while True:
        mbot2.servo_set(88.4,"all")
        time.sleep(0.2)
        mbot2.servo_set(95,"all")
        time.sleep(0.2)