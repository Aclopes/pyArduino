# https://realpython.com/arduino-python/#reading-analog-inputs

import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

new_analog_value = 0
old_analog_value = 0

while True:
    new_analog_value = analog_input.read()
    if new_analog_value:
        # This if is to avoid the program to print same thing all the time.
        if round(new_analog_value,2) != round(old_analog_value,2):
            print(new_analog_value)
            old_analog_value = new_analog_value
    time.sleep(0.2)