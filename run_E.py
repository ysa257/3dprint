import stepper
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="E-motor", description='Runs E-motor to desired position')

    parser.add_argument('--dir',default=1, type=int)
    parser.add_argument('--t', default=0.1,type=float)
    parser.add_argument('--v', default=0.7,type=float)

    args = parser.parse_args()

    direct = args.dir
    duration = args.t
    speed = args.v
    duration = 0.1
    
    stepper.move_motor(40,36,38,32,speed,duration,direct) #extrusion
