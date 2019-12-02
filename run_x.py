import stepper
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="x-motor", description='Runs x-motor to desired position')

    parser.add_argument('--dir',default=-1, type=int)
    parser.add_argument('--t', default=3,type=float)
    parser.add_argument('--v', default=0.001,type=float)

    args = parser.parse_args()
    
    ## bw - 34,2s   15,1s
    ## fw - 34,2s   18,1s   50,3s
    
    direct = args.dir
    duration = args.t
    speed = args.v
    stepper.move_motor(5,3,8,7,speed,duration,direct) # motor_x, asdf=-1 makes x sensor distance greater
