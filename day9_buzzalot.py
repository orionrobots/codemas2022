# Imports
from machine import Pin, PWM
import time

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Set PWM frequency to 1000
buzzer.freq(1000)

while True: # Run forever
    
    time.sleep(0.01) # Short delay
    
    if tilt.value() == 1: # If sensor is HIGH
        
        print("***TILT DETECTED***") # Print a string
        
        buzzer.duty_u16(10000) # Set duty (volume up)
        
        time.sleep(0.2) # Short delay
        
        buzzer.duty_u16(0) # Duty to zero (volume off)
