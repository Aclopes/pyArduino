import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')

board.digital[13].write(1)
time.sleep(1)
board.digital[13].write(0)
time.sleep(0.1)
board.digital[13].write(1)
time.sleep(1)
board.digital[13].write(0)
time.sleep(0.1)
board.digital[13].write(1)
time.sleep(0.5)
board.digital[13].write(0)
time.sleep(0.1)
board.digital[13].write(1)
time.sleep(0.5)
board.digital[13].write(0)
time.sleep(0.1)
print(".")

