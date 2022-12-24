# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
strip[0] = (255,0,0)
strip[1] = (0,255,0)
strip[2] = (0,0,255)
strip[3] = (255,0,255)
strip[4] = (255,255,0)

# Send the data to the strip
strip.write()