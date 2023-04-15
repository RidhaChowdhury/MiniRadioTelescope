from ControlBoard.port_wrapper import PortWrapper, FakePortWrapper

DEBUG_FAKE_PORT = False

# Commands to PCB:
EOT = chr(4).encode('ASCII')

CALIBRATE_ALT = 'cl'.encode('ASCII')
CALIBRATE_AZ = 'cz'.encode('ASCII')
CALIBRATE_TWIST = 'ct'.encode('ASCII')

MOVE_ALT_PLUS = 'ml'.encode('ASCII')
MOVE_ALT_PLUS = 'wl'.encode('ASCII')
MOVE_AZ_PLUS = 'mz'.encode('ASCII')
MOVE_AZ_MINUS = 'wz'.encode('ASCII')

GOTO_ALT_AZ = 'g '.encode('ASCII')

STOP_ALT = 'xl'.encode('ASCII')
STOP_AZ = 'xz'.encode('ASCII')
STOP_ALL = 'xa'.encode('ASCII')
GET_STATUS = 'r '.encode('ASCII')

def encode_degrees(num):
    if num < 0:
        raise Exception('Negative numbers are not supported; are you sure you want to move {} degrees?'.format(num))
    if isinstance(num, int):
        encoding = num % 360 * 10
    elif isinstance(num, float):
        encoding = round(num % 360 * 10)
    else:
        raise Exception('Unknown argument type num: {} Expected float or int.'.format(type(azimuth)))
    print(encoding)
    return encoding.to_bytes(2, byteorder='big')

def encode_calibrate_azimuth(azimuth): return CALIBRATE_AZ + encode_degrees(azimuth) + EOT
def encode_calibrate_altitude(altitude): return CALIBRATE_ALT + encode_degrees(altitude) + EOT
def encode_calibrate_twist(twist): return CALIBRATE_TWIST + encode_degrees(twist) + EOT

def encode_move_alt_plus(offset): return MOVE_ALT_PLUS + encode_degrees(offset) + EOT
def encode_move_alt_minus(offset): return MOVE_ALT_MINUS + encode_degrees(offset) + EOT
def encode_move_az_plus(offset): return MOVE_AZ_PLUS + encode_degrees(offset) + EOT
def encode_move_az_minus(offset): return MOVE_AZ_MINUS + encode_degrees(offset) + EOT

def encode_goto(altitude, azimuth): return GOTO_ALT_AZ + encode_degrees(altitude) + encode_degrees(azimuth) + EOT

class PCBWrapper:
    def calibrate_altitude(self, altitude): self.port.write(encode_calibrate_altitude(altitude))
    def calibrate_azimuth(self, azimuth): self.port.write(encode_calibrate_azimuth(azimuth))
    def goto(self, altitude, azimuth): self.port.write(encode_goto(altitude, azimuth))

    def move_alt(self, offset):
        if offset >= 0:
            self.port.write(encode_move_alt_plus(offset))
        else:
            self.port.write(encode_move_alt_minus(offset))
    def mov_az(self, offset):
        if offset >= 0:
            self.port.write(encode_move_az_plus(offset))
        else:
            self.port.write(encode_move_az_minus(offset))

    def stop(self): self.port.write(STOP_ALL + EOT)
    def stop_altitude(self): self.port.write(STOP_ALT + EOT)
    def stop_azimuth(self): self.port.write(STOP_AZ + EOT)

    def get_status(self):
        self.port.write(GET_STATUS + EOT)

    def __enter__(self):
        if DEBUG_FAKE_PORT:
            self.port_manager = FakePortWrapper()
        else:
            self.port_manager = PortWrapper()
        self.port = self.port_manager.__enter__()
        return self

    def __exit__(self, exception_type, exception, traceback):
        self.port_manager.__exit__(exception_type, exception, traceback)

def main():
    with PCBWrapper() as pcb:
        pcb.calibrate_azimuth(22.13)

if __name__ == '__main__':
    main()

