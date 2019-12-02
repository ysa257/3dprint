import stepper
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="y-motor", description='Runs y-motor to desired position')

    parser.add_argument('--dir', default=1,type=int)
    parser.add_argument('--t', default=4,type=float)
    parser.add_argument('--v', default=0.001,type=float)

    args = parser.parse_args()

    direct = args.dir
    duration = args.t
    speed = args.v
    
    #duration = 6
    #speed = 0.4
    #direct = -direct

    stepper.move_motor(10,15,11,12,speed,duration,direct) # motor_y
