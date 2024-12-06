import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button_pin = digitalio.DigitalInOut(board.GP17)
button_pin.direction = digitalio.Direction.INPUT

keyboard = Keyboard(usb_hid.devices)
keyboard_enabled = False

last_keypress_time = time.monotonic()
keypress_interval = 0.001

while True:
    if button_pin.value:
        keyboard_enabled = not keyboard_enabled
        time.sleep(0.1)

    if keyboard_enabled:
        led.value = True

        current_time = time.monotonic()
        
        if current_time - last_keypress_time >= keypress_interval:

            print(f"Sending G at {current_time}")

            keyboard.press(Keycode.G)
            time.sleep(0.1)
            keyboard.release_all()

            last_keypress_time = current_time

    else:
        led.value = False
        print("Keyboard disabled")


    time.sleep(0.05)
