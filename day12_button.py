# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define our button pin
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue= 0,0,255

# Define colour list
colours = [red, green, blue]

# Create index variable starting at 0
myindex = 0

# Variable with the number of items in our list (3)
# We -1 as the index starts at 0, and we want to use this for the colour list index number (0, 1 or 2)
# This is useful as it means we don't have to count the colours if we add more
indexlength = len(colours) -1

while True: # Run forever
    
    time.sleep(0.4) # Delay
    
    if button() == 1: # If button pressed
        
        # If the index variable is less than or equal to the lengh of the index
        if myindex < indexlength:
            
            # Add +1 to the index variable
            myindex = myindex + 1
        
        # If the index variable is over the index length
        else:
            
            # Set index variable back to 0 (the first item in our list)
            myindex = 0
            
        ## Now this code runs AFTER the if statements...
        
        # Fill the strip with the current list index colour
        strip.fill((colours[myindex]))
            
        # Write the data to the LED strip
        strip.write()
