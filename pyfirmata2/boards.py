BOARDS = {
    'arduino': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(6)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_mega': {
        'digital': tuple(x for x in range(54)),
        'analog': tuple(x for x in range(16)),
        'pwm': tuple(x for x in range(2, 14)),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_due': {
        'digital': tuple(x for x in range(54)),
        'analog': tuple(x for x in range(12)),
        'pwm': tuple(x for x in range(2, 14)),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'arduino_nano': {
        'digital': tuple(x for x in range(14)),
        'analog': tuple(x for x in range(8)),
        'pwm': (3, 5, 6, 9, 10, 11),
        'use_ports': True,
        'disabled': (0, 1)  # Rx, Tx, Crystal
    },
    'esp32': {
        'digital': tuple(x for x in range(34)),
        'analog': (0, 2, 4, 12, 13, 14, 15) + tuple(range(25, 34)),
        'pwm': tuple(x for x in range(34)), # Need to test this
        'use_ports': True,
        'disabled': (1, 3, 32, 33) + tuple(range(6, 12)),  # uart(1,3) Crystal(32,33) flash
    },
    'esp32s3': {
        'digital': tuple(x for x in range(49)),
        'analog': tuple(x for x in range(1,21)),
        'pwm': tuple(x for x in range(49)), # Need to test this
        'use_ports': True,
        'disabled': (15, 16, 19, 20, 43, 44) + tuple(range(26, 39))  # xtal(15,16) usb (19,20) psram (26 to 38) uart0 (43,44)
    },
}
