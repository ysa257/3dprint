import os
import pygcode

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
	file = "fakebearing.STL"
	run_printer(file)
