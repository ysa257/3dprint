import numpy as np
from gpiozero import DistanceSensor
import stepper

def move_xy(xcurrent,ycurrent,x,y):

	echo_pin_x = something
	trigger_pin_x = something
	echo_pin_y = something
	trigger_pin_y = something
	x_sensor = DistanceSensor(echo=echo_pin_x,trigger=trigger_pin_x)
	y_sensor = DistanceSensor(echo=echo_pin_y,trigger=trigger_pin_y)

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




