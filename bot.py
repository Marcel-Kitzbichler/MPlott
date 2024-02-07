import event, time, cyberpi, mbuild, mbot2
import time
#--------------------Settings-----------------------
stepsPerPixel = 14
pixelHeight = 3
rowLength = 12
forwardSpeed = 10
backwardSpeed = 10
setAngle = -4
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
drawInstance = False


def forward(servo):
    mbot2.turn(setAngle)
    mbot2.EM_reset_angle("EM1")
    mbot2.servo_set(upPos,"S1")
    if servo:
        cyberpi.broadcast("handleServo")
    mbot2.forward(10)
    while ((mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1))):
      pass
    mbot2.EM_stop("ALL")
    if (mbuild.quad_rgb_sensor.is_color("white","L2",1)) or (mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1)):
      while ((mbuild.quad_rgb_sensor.is_color("white","L2",1)) or (mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1))):
        mbot2.turn(4)
    else:
      while ((mbuild.quad_rgb_sensor.is_color("white","R2",1)) or (mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1))):
        mbot2.turn(-4)
    cyberpi.stop_other()
    mbot2.servo_set(upPos,"S1")


def back():
    mbot2.straight(rowLength*-1,backwardSpeed)

def drawLine():
    forward(True)
    back()

def drwImg():
    global currLine
    lineNumb = 0
    for i in imgBuffer:
        currLine = i
        drawPerc(lineNumb)
        for a in range(pixelHeight):
            drawLine()
        lineNumb += 1

def drawPerc(perc):
    percStr = str(perc * 10)
    text = cyberpi.sprite()
    text.move_to(64, 64)
    text.draw_text(percStr + "%")
    cyberpi.screen.render()
    text.delete()


@event.is_press('b')
def main():
    global drawInstance
    if drawInstance:
        cyberpi.stop_this()
    drawInstance = True
    time.sleep(2)
    forward(False)
    drwImg()
    drawInstance = False

@event.receive("handleServo")
def servoHandler():
    while True:
        pixel = int(mbot2.EM_get_angle("EM1")/stepsPerPixel)
        if pixel > len(currLine)-1:
            mbot2.servo_set(upPos,"S1")
            cyberpi.stop_this()
        i = currLine[9 - pixel]
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
    renderAtCursor(200)
    y = int((cursor.get_y()-10)/10)
    x = int((cursor.get_x()-10)/10)
    imgBuffer[y][x] = True

@event.is_press('a')
def earease():
    global imgBuffer
    global drawInstance
    if drawInstance:
        cyberpi.stop_other()
        mbot2.servo_set(upPos,"S1")
        drawInstance = False
        cyberpi.stop_all()
    renderAtCursor(0)
    y = int((cursor.get_y()-10)/10)
    x = int((cursor.get_x()-10)/10)
    imgBuffer[y][x] = False

def renderAtCursor(brightness):
    cyberpi.sketch.move_to(cursor.get_x(), cursor.get_y())
    cyberpi.sketch.set_color(brightness,brightness,brightness)
    cyberpi.sketch.start()
    cyberpi.sketch.move_x(1)
    cyberpi.sketch.end()
    cyberpi.screen.render()