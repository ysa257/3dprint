import os
import pygcode
import xy_movement
import stepper
import RPi.GPIO as GPIO
from time import sleep
from tkinter import *
from sensortest import calculate_distance_5_times

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
    file = "CatHeadTest.STL"
    coords = scan_stl(file)
    E_des = 0
    #GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    
    #GPIO.setup(10, GPIO.OUT)
    #GPIO.setup(15, GPIO.OUT)
    #GPIO.setup(11, GPIO.OUT)
    #GPIO.setup(12, GPIO.OUT)
    #GPIO.setup(5, GPIO.OUT)
    #GPIO.setup(3, GPIO.OUT)
    #GPIO.setup(8, GPIO.OUT)
    #GPIO.setup(7, GPIO.OUT)
    #GPIO.setup(40, GPIO.OUT)
    #GPIO.setup(36, GPIO.OUT)
    #GPIO.setup(38, GPIO.OUT)
    #GPIO.setup(32, GPIO.OUT)
    
    #coords

    #x_sensor = DistanceSensor(echo=echo_pin_x,trigger=trigger_pin_x)
    #y_sensor = DistanceSensor(echo=echo_pin_y,trigger=trigger_pin_y)

    #print(calculate_distance(29,31))
    #print(calculate_distance(26,21))
    #print(calculate_distance(26,21))
    #print(calculate_distance(26,21))
    #print(calculate_distance(26,21))
    #print(calculate_distance(26,21))
    #print(calculate_distance(26,21))
    
    echo_pin_x = 26
    trigger_pin_x = 21
    echo_pin_y = 29
    trigger_pin_y = 31
    #x_o = calculate_distance_5_times(echo_pin_x,trigger_pin_x)
    #y_o = calculate_distance_5_times(echo_pin_y,trigger_pin_y)
    #xy_movement.move_xy_5_sec()
    #x_n = calculate_distance_5_times(echo_pin_x,trigger_pin_x)
    #y_n = calculate_distance_5_times(echo_pin_y,trigger_pin_y)
    v_x = 22.5
    v_y = 2.25
    #print(x_n-x_o)
    #v_x = (x_n - x_o)/5
    #v_y = (y_n - y_o)/5
    
    #v_x = 0.1


    for step in coords:
        step
        
        if step<4:
            if coords[step][0]!='':
                x_des = coords[step][0]
                x_old = x_des
            if coords[step][1]!='':
                y_des = coords[step][1]
                y_old = y_des
            if coords[step][2]!='':
                E_des = coords[step][2]
                E_old = E_des

    
                
                
                
        if step>5:
            print(x_old)
            print(y_old)
            print(E_old)
            
            x_des, y_des, E_des = coords[step]
            
            if coords[step][0] =='':
                x_des = x_old
            if coords[step][1]=='':
                y_des = y_old
            if coords[step][2]=='':
                E_des = E_old
            
            x = x_des - x_old
            y = y_des - y_old
            E = E_des - E_old
        
            xy_movement.move_xy(x,y,E,v_x,v_y)
        
            x_old = x_des
            y_old = y_des
            E_old = E_des
    #stepper.move_motor(10,15,11,12,0.2,10,1) # motor_y
    #stepper.move_motor(5,3,8,7,0.05,5,-1) # motor_x, asdf=-1 makes x sensor distance greater
    #stepper.move_motor(40,36,38,32,0.2,5,-1) #extrusion
    
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
    

    
