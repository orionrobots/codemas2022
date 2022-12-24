from machine import ADC, Pin
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up our LED names and GPIO pin numbers
amber = Pin(18, Pin.OUT)
red = Pin(20, Pin.OUT)
green = Pin(19, Pin.OUT)
mydelay = 0

while True:
    # Update our variable with the reading divided by 65000
    mydelay = potentiometer.read_u16() / 65000

    red.value(1)
    amber.value(0)
    green.value(0)
    
    time.sleep(mydelay)
    
    # LEDs all off
    red.value(0)
    amber.value(1)
    green.value(0)
    
    time.sleep(mydelay)
    
    # LEDs all on
    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(mydelay)
