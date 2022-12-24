# Imports
import time
# Download from https://github.com/python/cpython/blob/3.11/Lib/colorsys.py
import colorsys
from machine import Pin, ADC
from neopixel import NeoPixel


# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)
potentiometer = ADC(Pin(26))

shift = 0

while True:
    shift_by = potentiometer.read_u16() / 65535
    # iterate over 15 leds
    for i in range(15):
        hue = (i/15) + shift_by
        while(hue > 1):
            hue -= 1
        rgb = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 0.8)]
        
        # Set each LED in the range to yellow
        strip[i] = rgb
    strip.write()
    time.sleep(0.1)
    
# Send the data to the strip


