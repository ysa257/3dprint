import stepper

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="E-motor", description='Runs E-motor to desired position')

    parser.add_argument('--dir', type=int)
    parser.add_argument('--t', type=int)
    parser.add_argument('--v', type=int)

    args = parser.parse_args()

    dir = args.dir
    duration = args.t
    speed = args.v

    stepper.move_motor(40,36,38,32,speed,duration,dir) #extrusion
