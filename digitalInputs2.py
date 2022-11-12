# https://realpython.com/arduino-python/#reading-digital-inputs

import pyfirmata
import time


board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

it = pyfirmata.util.Iterator(board)
it.start()

# instead this board.digital[10].mode = pyfirmata.INPUT:
led = board.get_pin('d:13:o')

# instead inform the Input het in a variable here:
digital_input = board.get_pin('d:10:i')

apertado = False
while True:
    # sw = board.digital[10].read()
    sw = digital_input.read()
    
    if sw is True:
        led.write(1)
        print("Apertou")
        apertado = True
    else:
        led.write(0)
        if apertado:
            print("Soltou!")
            apertado = False
    time.sleep(0.1)