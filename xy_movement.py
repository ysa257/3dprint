#import numpy as np
import stepper
import os
import sensortest
import RPi.GPIO as GPIO
import time

def move_xy_5_sec():
    command = "python3 stepper.py --E_motor=0 --E_motor_direction=1 --E_motor_duration=0 --x_motor=1 --x_motor_direction=1 --x_motor_duration=5 --y_motor=1 --y_motor_direction=1 --y_motor_duration=5"
    os.system(command)
    GPIO.cleanup()

def move_xy(x,y,E,v_x,v_y):

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
    t = str(0.1) #motor step duration
    t_x = x/v_x
    t_y = y/v_y


    



    command=""

    if x>0:
        command = "python3 stepper.py --x_motor=1 --x_motor_direction=1 --x_motor_duration=" + str(t_x)
    elif x<0:
        command = "python3 stepper.py --x_motor=1 --x_motor_direction=-1 --x_motor_duration=" + str(-t_x)
    
    if command!="":
        os.system(command)
        start = time.time()
        
        while time.time() - start < abs(t_x):
            start
    
    command = ""
    
    if y>0:
        command = "python3 stepper.py --y_motor=1 --y_motor_direction=1 --y_motor_duration=" + str(t_y)
    elif y<0:
        command = "python3 stepper.py --y_motor=1 --y_motor_direction=-1 --y_motor_duration=" + str(-t_y)

        #if E>0 and move==0:
    if command!= "":
        os.system(command)
        start = time.time()
    
        while time.time() - start < abs(t_y):
            start
    command = ""
    
    if E!= 0:
        command =  "python3 stepper.py --E_motor=1 --E_motor_direction=1 --E_motor_duration=" + t
    
        os.system(command)

        start = time.time()
    
        while time.time() - start < abs(float(t)):
            start

    GPIO.cleanup()
