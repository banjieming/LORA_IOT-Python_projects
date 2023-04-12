"""TouchPad Demo."""
from time import sleep

from machine import Pin, TouchPad
thresholdR = []
thresholdG = []
thresholdB = []
touchR = TouchPad(Pin(4))
touchG = TouchPad(Pin(27))
touchB = TouchPad(Pin(33))
LEDR = Pin(14, Pin.OUT)
LEDG = Pin(12, Pin.OUT)
LEDB = Pin(13, Pin.OUT)

def flashLED(led):
	for i in range(3):
		led.value(1)
		sleep(.7)
		led.value(0)
		sleep(.3)

# Scan each TouchPad 12 times for calibration
for x in range(12):
    thresholdR.append(touchR.read())
    thresholdG.append(touchG.read())
    thresholdB.append(touchB.read())
    sleep(.1)

# Store average threshold values
thresholdR = sum(thresholdR) // len(thresholdR)
thresholdG = sum(thresholdG) // len(thresholdG)
thresholdB = sum(thresholdB) // len(thresholdB)
print('ThresholdR: {0}'.format(thresholdR))
print('ThresholdG: {0}'.format(thresholdG))
print('ThresholdB: {0}'.format(thresholdB))

try:
    while True:
        capacitanceR = touchR.read()
        capacitanceG = touchG.read()
        capacitanceB = touchB.read()
        cap_ratioR = capacitanceR / thresholdR
        cap_ratioG = capacitanceG / thresholdG
        cap_ratioB = capacitanceB / thresholdB
        # Check if a TouchPad is pressed
        if .40 < cap_ratioR < .95:
            flashLED(LEDR)
            print('TouchR: {0}, Diff: {1}, Ratio: {2}%.'.format(
                  capacitanceR, thresholdR - capacitanceR, cap_ratioR * 100))
            sleep(.2)  # Debounce press
        if .40 < cap_ratioG < .95:
            flashLED(LEDG)
            print('TouchG: {0}, Diff: {1}, Ratio: {2}%.'.format(
                  capacitanceG, thresholdG - capacitanceG, cap_ratioG * 100))
            sleep(.2)  # Debounce press
        if .40 < cap_ratioB < .95:
            flashLED(LEDB)
            print('TouchB: {0}, Diff: {1}, Ratio: {2}%.'.format(
                  capacitanceB, thresholdB - capacitanceB, cap_ratioB * 100))
            sleep(.2)  # Debounce press            

except KeyboardInterrupt:
    print('\nCtrl-C pressed.  Cleaning up and exiting...')
finally:
    sleep(.1)