import os
import pygcode
import xy_movement
import stepper
import RPi.GPIO as GPIO
from time import sleep
from tkinter import *
from sensortest import calculate_distance

def scan_stl(stl_filename):
    gcode_filename = stl_filename[:-4] + ".gcode"
    command = "mandoline -o " + gcode_filename + " " + stl_filename
    gcode_filename
    os.system(command)

    start_scan = 0
    coords = dict()


    with open(gcode_filename,'r') as file:
        count = 0
        for line_text in file.readlines():

            start_x = 0
            start_y = 0
            start_E = 0

            x = str()
            y = str()
            E = str()

            if "( Nozzle 0 )" in line_text:
                start_scan = 1
            if start_scan:
                line = pygcode.Line(line_text)
                print(line)
                for char in str(line):
                    if char==' ':
                        start_x = 0
                        start_y = 0
                        start_E = 0

                    elif start_x:
                        x = x + char
                    elif start_y:
                        y = y + char
                    elif start_E:
                        E += char

                    if char=='X':
                        start_x = 1
                    elif char=='Y':
                        start_y = 1
                    elif char=='E':
                        start_E = 1


                if x!='' and y!='' and E!='':
                    coords[count] = [float(x),float(y),float(E)]
                    count += 1
            else:
                line_text

    return coords



if __name__ == "__main__":
    file = "fakebearing.STL"
    #coords = scan_stl(file)
    E_des = 0
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    

    #x_sensor = DistanceSensor(echo=echo_pin_x,trigger=trigger_pin_x)
    #y_sensor = DistanceSensor(echo=echo_pin_y,trigger=trigger_pin_y)

    
    #for step in coords:
        #step

        #x_des, y_des, E_new = coords[step]

        
        #xy_movement.move_xy(x_des,y_des, E_des-E_new)
        
        #E_des = E_new
    stepper.move_motor(10,15,11,12,0.05,5,-1) # motor_y
    #stepper.move_motor(5,3,8,7,0.05,5,-1) # motor_x, asdf=-1 makes x sensor distance greater
    #stepper.move_motor(40,36,38,32,0.05,5,-1) #extrusion
    
#    while True:
#        print('xdist: ', x_sensor.distance*1000)
#        print('ydist: ', y_sensor.distance*1000)
#        sleep(1)

    # 0 is left button, 1 is center, 2 is right button
    # GPIO.cleanup()
    #
    # bh = 10 #button height
    # bw = 21 #button width
    # # stepper.move_all_motors(10,11,15,12,5,8,3,7,40,38,36,32,0.1,7,-1)
    #stepper.move_all_motors(10,15,11,12,5,3,8,7,40,36,38,32,0.05,3,1)
    #
    GPIO.cleanup()
    # leftbutt = Button()
    # midbutt = Button()
    # rightbutt = Button()
    # xsensor = DistanceSensor(echo=,trigger=)
    # ysensor = DistanceSensor(echo=,trigger=)
    

    
