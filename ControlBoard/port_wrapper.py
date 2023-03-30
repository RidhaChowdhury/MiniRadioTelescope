from pyftdi.ftdi import Ftdi
from pyftdi.usbtools import UsbTools
from pyftdi.ftdi import Ftdi
from pyftdi.usbtools import UsbTools

import pyftdi.serialext

BAUD = 3_000_000

# Hacked together from pyftdi.ftdi.Ftdi.show_devices()
#  and pyftdi.usbtools.UsbTools.show_devices().
# Original source code from their repository, https://github.com/eblot/pyftdi/tree/master/pyftdi
def get_device_strings():
    vdict = Ftdi.VENDOR_IDS
    pdict = Ftdi.PRODUCT_IDS
    default_vendor = Ftdi.DEFAULT_VENDOR
    devdescs = UsbTools.list_devices('ftdi:///?', vdict, pdict, default_vendor)
    devstrs = UsbTools.build_dev_strings('ftdi', vdict, pdict, devdescs)
    return devstrs

def get_device_urls():
    return [url for url, _ in get_device_strings()]

# Use 'with PortWrapper() as port:' context manager.
# If you instantiate this class and forget to wrapper.port.close(),
#  you will get errors where the chip stops responding until you unplug & plug it.
class PortWrapper:
    def __init__(self):
        urls = get_device_urls()
        if len(urls) == 0:
            raise Exception('Could not find any FTDI devices plugged into your computer.')
        if len(urls) > 1:
            raise Exception('Found multiple FTDI devices plugged into your computer; please rewrite this program to select one.')
        url ,= urls
        self.port = pyftdi.serialext.serial_for_url(url, baudrate=BAUD)
    
    def __enter__(self):
        return self.port
    
    def __exit__(self, exception_type, exception, traceback):
        self.port.close()

def main():
    print('Opening the FT232 device...')
    with PortWrapper() as port:
        message = b'Hello, World!'
        print('Writing {} to the device...'.format(repr(message)))
        port.write(message)
        print('Reading from the device...')
        print(' If this program freezes here, you may have unclosed connections to the chip,')
        print('  and should unplug and replug the device.')
        print(' If you do not use the "with PortWrapper() as port" context manager,')
        print('  make sure you manually called port_wrapper.port.close().')
        print(' Or it may freeze if your chip does not echo responses;')
        print('  make sure tx and rx are shorted.')
        response = port.read(len(message))
        print('Response is {}'.format(repr(response)))

if __name__ == '__main__':
    main()
