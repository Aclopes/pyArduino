# https://realpython.com/arduino-python/#reading-analog-inputs

import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led_red = board.get_pin('d:13:o')
led_blue = board.get_pin('d:10:o')

analog_value = 0

while True:
    analog_value = analog_input.read()
    if analog_value is not None:
        delay = analog_value + 0.1
        led_red.write(1)
        led_blue.write(0)
        time.sleep(delay)
        led_red.write(0)
        led_blue.write(1)
        time.sleep(delay)
    else:
        time.sleep(0.2)