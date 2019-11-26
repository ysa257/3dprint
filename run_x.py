import stepper

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="x-motor", description='Runs x-motor to desired position')

    parser.add_argument('--dir', type=int)
    parser.add_argument('--t', type=int)
    parser.add_argument('--v', type=int)

    args = parser.parse_args()

    dir = args.dir
    duration = args.t
    speed = args.v

    stepper.move_motor(5,3,8,7,speed,duration,dir) # motor_x, asdf=-1 makes x sensor distance greater
