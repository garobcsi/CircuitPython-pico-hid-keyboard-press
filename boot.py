import board
import digitalio
import usb_hid
import storage
import time
import supervisor

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

storage_button = digitalio.DigitalInOut(board.GP14)
storage_button.direction = digitalio.Direction.INPUT

if storage_button.value:
    storage.enable_usb_drive()
    supervisor.set_usb_console(True)
else:
    storage.disable_usb_drive()
    supervisor.set_usb_console(False)

    usb_hid.enable(usb_hid.Device.KEYBOARD)