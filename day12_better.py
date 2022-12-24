# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# iterate over 15 leds
for i in range(15):
    
    # Set each LED in the range to yellow
    strip[i] = (255,0,255)

# Send the data to the strip
strip.write()
