import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Set up the built-in LED on the Pico
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Set up the keyboard emulation
keyboard = Keyboard(usb_hid.devices)

# Main loop
while True:
    # Blink the LED (quick blink)
    led.value = True
    time.sleep(0.1)

    # Send the letter 'G' key press
    keyboard.press(Keycode.G)
    time.sleep(0.1)  # Hold key for a short time
    keyboard.release_all()

    led.value = False
    time.sleep(0.1)

    #Add a delay to control how often the "G" key is sent
    time.sleep(10)  # Wait 1 second before repeating