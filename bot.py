import event, time, cyberpi, mbuild, mbot2
import time


def forward():
    mbot2.servo_set(87,"all")
    mbot2.straight(10)
    mbot2.servo_set(95,"all")


def back():
    mbot2.turn(2)
    mbot2.straight(-10)
    mbot2.turn(-2)

def drawLine():
    forward()
    back()


@event.start
def main():
    mbot2.servo_set(95,"all")
    time.sleep(1)
    while True:
        drawLine()