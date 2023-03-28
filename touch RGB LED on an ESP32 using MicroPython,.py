from machine import TouchPad, Pin, PWM
import time

# Set up the RGB LED pins and touch sensor pins
red_pin = PWM(Pin(14))
green_pin = PWM(Pin(13))
blue_pin = PWM(Pin(12))
touch_pad = TouchPad(Pin(4))

# Set a threshold value for the touch sensor
threshold = 200

# Main loop
while True:
    # Read the value of the touch sensor
    touch_value = touch_pad.read()

    # Adjust the RGB LED based on the touch sensor value
    if touch_value < threshold:
        # If the touch value is below the threshold, turn the LED red
        red_pin.duty(512)
        green_pin.duty(0)
        blue_pin.duty(0)
    elif touch_value < (threshold * 2):
        # If the touch value is between the threshold and twice the threshold, turn the LED green
        red_pin.duty(0)
        green_pin.duty(512)
        blue_pin.duty(0)
    else:
        # If the touch value is above twice the threshold, turn the LED blue
        red_pin.duty(0)
        green_pin.duty(0)
        blue_pin.duty(512)

    # Wait for a short period of time before looping again
    time.sleep(0.1)