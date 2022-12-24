# Imports
from machine import Pin, I2C
# SSD1306 from https://thepihut.com/blogs/raspberry-pi-tutorials/maker-advent-calendar-day-11-omg-oled
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1)

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

# Write three lines to the display
display.text("¯\_(ツ)_/¯",0,0)
display.text("I dunno",50,12)
display.text(":) in a pear tree...",0,24)

# Update the display
display.show()
