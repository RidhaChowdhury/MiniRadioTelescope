import argparse

from ControlBoard.protocol_wrapper import PCBWrapper

def main(args):
    with PCBWrapper() as pcb:
        if args['stop']:          pcb.stop()
        if args['stop_altitude']: pcb.stop_altitude()
        if args['stop_azimuth']:  pcb.stop_azimuth()

        if args['calibrate_twist']:
            pcb.calibrate_twist(args['calibrate_twist'])

        alt, az = args['altitude'], args['azimuth']
        if args['calibrate']:
            if not alt is None: pcb.calibrate_altitude(alt)
            if not az  is None: pcb.calibrate_azimuth(az)
        elif args['move']:
            if not alt is None: pcb.move_alt(alt)
            if not az  is None: pcb.move_az(az)
        elif not alt is None and not az is None:
            pcb.goto(alt, az)
        
        if args['get_status']:
            print('Status:', pcb.get_status())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='MiniRadioTelescope controller',
        description='Perform an action with the radio telescope as specified by the command line arguments.'
    )
    parser.add_argument('-s', '--stop', action='store_true')
    parser.add_argument('-sl', '--stop_altitude', action='store_true')
    parser.add_argument('-sz', '--stop_azimuth', action='store_true')
    parser.add_argument('-ct', '--calibrate_twist')
    parser.add_argument('-l', '--altitude')
    parser.add_argument('-z', '--azimuth')
    parser.add_argument('-c', '--calibrate', action='store_true')
    parser.add_argument('-m', '--move', action='store_true')
    parser.add_argument('-g', '--get_status', action='store_true')
    args = parser.parse_args()
    args = vars(args)

    alt, az = args['altitude'], args['azimuth']
    twist = args['calibrate_twist']
    c, m = args['calibrate'], args['move']

    if (alt is None) != (az is None) and not (c or m):
        raise Exception('Cannot at this time goto altitude independently from azimuth. You must choose both.')
    
    if c and m:
        raise Exception('Cannot calibrate and move at the same time. You must run them as separate commands.')
    
    if not az is None:    args['azimuth'] = float(az)
    if not alt is None:   args['altitude'] = float(alt)
    if not twist is None: args['calibrate_twist'] = float(twist)
    
    main(args)


