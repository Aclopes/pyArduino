# https://realpython.com/arduino-python/#reading-digital-inputs

import pyfirmata
import time


board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[10].mode = pyfirmata.INPUT
apertado = False
while True:
    sw = board.digital[10].read()
    if sw is True:
        board.digital[13].write(1)
        print("Apertou")
        apertado = True
    else:
        board.digital[13].write(0)
        if apertado:
            print("Soltou!")
            apertado = False
    time.sleep(0.1)