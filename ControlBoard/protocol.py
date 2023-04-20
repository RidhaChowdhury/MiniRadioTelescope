EOT = chr(4).encode('ASCII')

CALIBRATE_ALT =   'cl'.encode('ASCII')
CALIBRATE_AZ =    'cz'.encode('ASCII')
CALIBRATE_TWIST = 'ct'.encode('ASCII')

MOVE_ALT_PLUS =   'ml'.encode('ASCII')
MOVE_ALT_MINUS =  'wl'.encode('ASCII')
MOVE_AZ_PLUS =    'mz'.encode('ASCII')
MOVE_AZ_MINUS =   'wz'.encode('ASCII')

GOTO_ALT_AZ =     'g '.encode('ASCII')

STOP_ALT =        'xl'.encode('ASCII')
STOP_AZ =         'xz'.encode('ASCII')
STOP_ALL =        'xa'.encode('ASCII')
GET_STATUS =      'r '.encode('ASCII')

FLAGS = [
    (1 << 15, "Bad command; start over"),
    (1 << 14, "Moving"),                    # Stationary by default
]
