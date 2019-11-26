#import numpy as np
import stepper
import os
import sensortest
import RPi.GPIO as GPIO

def move_xy(x,y,E):

    echo_pin_x = 26#7#9 # 21
    trigger_pin_x = 21#9#7 # 26
    echo_pin_y = 29#5#5 # 29
    trigger_pin_y = 31#6#6 # 31

    move = 1

    #gpiozero framework:
    #
    #x_sensor = DistanceSensor(echo=echo_pin_x,trigger=trigger_pin_x)
    #y_sensor = DistanceSensor(echo=echo_pin_y,trigger=trigger_pin_y)

    res = 0.1 #resolution
    t = 0.1 #motor step duration


    while move:
        command = "python3 stepper.py "

        xcurrent = sensortest.calculate_distance(echo_pin_x, trigger_pin_x) #needs calibration
        ycurrent = sensortest.calculate_distance(echo_pin_y, trigger_pin_y) #needs calibration

        if (xcurrent<x-res):
            command = command + "--x_motor=1 --x_motor_direction=1 --x_motor_duration=" + t
        elif (xcurrent>x+res):
            command = command + "--x_motor=1 --x_motor_direction=-1 --x_motor_duration=" + t

        if (ycurrent<y-res):
            command = command + "--y_motor=1 --y_motor_direction=1 --y_motor_duration=" + t
        elif (ycurrent>y+res):
            command = command + "--y_motor=1 --y_motor_direction=-1 --y_motor_duration=" + t

        if E>0:
            command = command + "--E_motor=1 --E_motor_direction=1 --E_motor_duration=" + t


        if xcurrent>x-res and xcurrent<x+res and ycurrent>y-res and ycurrent<y+res:
            move = 0

    os.system(command)

    GPIO.cleanup()
