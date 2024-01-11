import event, time, cyberpi, mbuild, mbot2
import time
#--------------------Settings-----------------------
stepsPerPixel = 14
pixelHeight = 4
rowLength = 12
forwardSpeed = 20
backwardSpeed = 20
setAngle = 3
resetAngle = -3
upPos = 95
downPos = 87.7
#---------------------------------------------------

imgBuffer =[
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False,False]
]
cursor = cyberpi.sprite()
currLine = []


def forward():
    mbot2.EM_reset_angle("EM1")
    mbot2.servo_set(upPos,"S1")
    cyberpi.broadcast("handleServo")
    mbot2.straight(rowLength,forwardSpeed)
    cyberpi.stop_other()
    mbot2.servo_set(upPos,"S1")


def back():
    mbot2.turn(setAngle)
    mbot2.straight(rowLength*-1,backwardSpeed)
    mbot2.turn(resetAngle)

def drawLine():
    forward()
    back()

def drwImg():
    global currLine
    for i in imgBuffer:
        currLine = i
        for a in range(pixelHeight):
            drawLine()


@event.is_press('b')
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


@event.start
def on_start():
    global cursor
    cursor.draw_pixel([0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0xffffff,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000,0x000000])
    cursor.move_to(10, 10)
    cyberpi.screen.render()

@event.is_press('right')
def cursorRight():
    if cursor.get_x() < 100:
        cursor.move_x(10)
        cyberpi.screen.render()

@event.is_press('left')
def cursorLeft():
    if cursor.get_x() > 10:
        cursor.move_x(-10)
        cyberpi.screen.render()

@event.is_press('up')
def cursorUp():
    if cursor.get_y() > 10:
        cursor.move_y(-10)
        cyberpi.screen.render()

@event.is_press('down')
def cursorDown():
    if cursor.get_y() < 100:
        cursor.move_y(10)
        cyberpi.screen.render()

@event.is_press('middle')
def draw():
    global imgBuffer
    cyberpi.sketch.move_to(cursor.get_x(), cursor.get_y())
    cyberpi.sketch.set_color(252, 3, 7)
    cyberpi.sketch.start()
    cyberpi.sketch.move_x(1)
    cyberpi.sketch.end()
    cyberpi.screen.render()
    y = int((cursor.get_y()-10)/10)
    x = int((cursor.get_x()-10)/10)
    imgBuffer[y][x] = True

@event.is_press('a')
def earease():
    global imgBuffer
    cyberpi.sketch.move_to(cursor.get_x(), cursor.get_y())
    cyberpi.sketch.set_color(0,0,0)
    cyberpi.sketch.start()
    cyberpi.sketch.move_x(1)
    cyberpi.sketch.end()
    cyberpi.screen.render()
    y = int((cursor.get_y()-10)/10)
    x = int((cursor.get_x()-10)/10)
    imgBuffer[y][x] = False