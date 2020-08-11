# Simple "Blink" script to flash a LED every second.

import pyfirmata
import time

# Establish serial connection. FInd the port in Arduino IDE.
board = pyfirmata.Arduino('COM4')

# Every second, flash the LED on digital pin 13
while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
