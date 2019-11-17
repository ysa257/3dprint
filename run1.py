import os
import pygcode
import xy_movement
import stepper
from tkinter import *

def run_printer(stl_filename):
	gcode_filename = stl_filename[:-4] + ".gcode"
	command = "mandoline -o " + gcode_filename + " " + stl_filename
	gcode_filename
	os.system(command)

	with open(gcode_filename,'r') as file:
		for line_text in file.readlines():
			if not ("Printing..." in line_text):
				line = pygcode.Line(line_text)
				print(line)
			else:
				line_text


if __name__ == "__main__":
	# file = "fakebearing.STL"
	# run_printer(file)


	# 0 is left button, 1 is center, 2 is right button

	bh = 10 #button height
	bw = 21 #button width
	stepper.move_all_motors(13,11,15,12,5,10,3,7,16,22,8,18,0.7,1)
	# leftbutt = Button()
	# midbutt = Button()
	# rightbutt = Button()
	# xsensor = DistanceSensor(echo=,trigger=)
	# ysensor = DistanceSensor(echo=,trigger=)

	
