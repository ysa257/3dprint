import os
import pygcode
import xy_movement
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

	# leftbutt = Button()
	# midbutt = Button()
	# rightbutt = Button()
	# xsensor = DistanceSensor(echo=,trigger=)
	# ysensor = DistanceSensor(echo=,trigger=)

	window = Tk()
	window.title("Print food")
	window.geometry('580x200')
	# left = Button(window, height=bh, width=bw, text="select file to print")
	# left.grid(column=0, row=0)
	# mid = Button(window, height=bh, width=bw, text="adjust parameters")
	# mid.grid(column=1, row=0)
	# right = Button(window, height=bh, width=bw, text="right")
	# right.grid(column=2, row=0)
	#
	# select = Button(window, height=bh, width=3*bw, text="select file to print")
	# select.grid(column=0, row=0)

	root = Tk()
	e = Entry(root)
	e.pack()


	def callback(*args):
		print(e.get())


	e.bind("<Return>", callback)

	root.mainloop()
	window.mainloop()