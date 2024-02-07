import event, time, cyberpi, mbot2, mbuild

@event.is_press('a')
def is_btn_press():
    cyberpi.stop_other()
    mbot2.forward(10)
    while not not ((mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1))):
      # DO SOMETHING
      pass

    mbot2.EM_stop("ALL")
    if (mbuild.quad_rgb_sensor.is_color("white","L2",1)) or (mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1)):
      while not not ((mbuild.quad_rgb_sensor.is_color("white","L2",1)) or (mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1))):
        mbot2.turn(4)

    else:
      while not not ((mbuild.quad_rgb_sensor.is_color("white","R2",1)) or (mbuild.quad_rgb_sensor.is_color("white","R2",1)) and (mbuild.quad_rgb_sensor.is_color("white","L2",1))):
        mbot2.turn(-4)

