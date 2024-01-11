import event, time, cyberpi

cursor = cyberpi.sprite()
bitmap =[
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

@event.is_press('a')
def draw():
    global bitmap
    cyberpi.sketch.move_to(cursor.get_x(), cursor.get_y())
    cyberpi.sketch.set_color(252, 3, 7)
    cyberpi.sketch.start()
    cyberpi.sketch.move_x(1)
    cyberpi.sketch.end()
    cyberpi.screen.render()
    y = int((cursor.get_y()-10)/10)
    x = int((cursor.get_x()-10)/10)
    bitmap[y][x] = True

@event.is_press('b')
def earease():
    global bitmap
    cyberpi.sketch.move_to(cursor.get_x(), cursor.get_y())
    cyberpi.sketch.set_color(0,0,0)
    cyberpi.sketch.start()
    cyberpi.sketch.move_x(1)
    cyberpi.sketch.end()
    cyberpi.screen.render()
    y = int((cursor.get_y()-10)/10)
    x = int((cursor.get_x()-10)/10)
    bitmap[y][x] = False


@event.is_press('middle')
def send():
    cyberpi.wifi_broadcast.set("bitmap", bitmap)