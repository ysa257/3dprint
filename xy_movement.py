import numpy as np
from gpiozero import DistanceSensor
import stepper
import os
import sensortest

def move_xy(x,y):

    echo_pin_x = 26#7#9 # 21
    trigger_pin_x = 21#9#7 # 26
    echo_pin_y = 29#5#5 # 29
    trigger_pin_y = 31#6#6 # 31
    #x_sensor = DistanceSensor(echo=echo_pin_x,trigger=trigger_pin_x)
    #y_sensor = DistanceSensor(echo=echo_pin_y,trigger=trigger_pin_y)

    if xcurrent>x and ycurrent>y:
        while x_sensor.distance>x and y_sensor.distance>y:
            stepper.move_two_motors()

    elif xcurrent>x and ycurrent<y:
        while x_sensor.distance>x and y_sensor.distance<y:
            stepper.move_two_motors()

    elif xcurrent<x and ycurrent>y:
        while x_sensor.distance<x and y_sensor.distance>y:
            stepper.move_two_motors()

    elif xcurrent<x and ycurrent<y:
        while x_sensor.distance<x and y_sensor.distance<y:
            stepper.move_two_motors()

    elif xcurrent==x and ycurrent<y:
        while y_sensor.distance<y:
            stepper.move_motor()

    elif xcurrent==x and ycurrent>y:
        while y_sensor.distance>y:
            stepper.move_motor()

    elif xcurrent>x and ycurrent==y:
        while x_sensor.distance>x:
            stepper.move_motor()

    elif xcurrent<x and ycurrent==y:
        while x_sensor.distance<x:
            stepper.move_motor()

    return x_sensor.distance, y_sensor.distance




