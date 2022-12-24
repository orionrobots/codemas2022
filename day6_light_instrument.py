# Imports
from machine import ADC, Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set up the LED pins
amber = Pin(18, Pin.OUT)
red = Pin(20, Pin.OUT)
green = Pin(19, Pin.OUT)

# Define pin for our sensor
lightsensor = ADC(Pin(26))


while True: # Run forever
    
    # Read sensor value and store it in a variable called 'light'
    light = lightsensor.read_u16()
    lightpercent = light/65535*100
    
    tone = int(1760 * lightpercent / 100)
    buzzer.duty_u16(10000)
    buzzer.freq(tone)
    
    print(f"{lightpercent:.1f}%")
    time.sleep(0.1)


    
