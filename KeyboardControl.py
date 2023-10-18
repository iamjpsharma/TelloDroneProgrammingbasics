from djitellopy import tello
import KeypressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
me.get_battery()


def getKeyboardInput():
    lr, fb, yd, yu = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yu = speed
    elif kp.getKey("d"):
        yu = -speed

    if kp.getKey("q"):
        me.land()

    if kp.getKey("e"):
        me.takeoff()


    return [lr, fb, yd, yu]

me.takeoff()



while True:
    print(kp.getKey("s"))
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)


