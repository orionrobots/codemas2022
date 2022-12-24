# Imports
from machine import Pin, PWM
import time

# Set up the LED pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13))

# Set PWM duty to 0% at program start
buzzer.duty_u16(0)
 
# Set up PIR pin with pull down
pir = Pin(26, Pin.IN, Pin.PULL_DOWN)


A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 698
Fs = 730
G = 784
Gs = 830

A2 = 440 * 2
As2 = 466 * 2
B2 = 494 * 2
C2 = 523 * 2
Cs2 = 554 * 2
D2 = 587 * 2
Ds2 = 622 * 2
E2 = 659 * 2
F2 = 698 * 2
Fs2 = 740 * 2
G2 = 784 * 2
Gs2 = 830 * 2

# Create volume variable (Duty cycle)
volume = 10000

# Create our function with arguments
def playtone(note,vol,delay1,delay2):
    red.value(1) # Red ON
    amber.value(1) # Amber ON
    green.value(1) # Green ON
    
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    
    red.value(0) # Red OFF
    amber.value(0) # Amber OFF
    green.value(0) # Green OFF    
    
    buzzer.duty_u16(0)
    time.sleep(delay2)

# Warm up/settle PIR sensor
print("Warming up...")
time.sleep(10) # Delay to allow the sensor to settle
print("Sensor ready!")

def alarm(): # Our alarm function
    
    # Set PWM duty (volume up)
    buzzer.duty_u16(10000)
    notes = [
        [G, 0.2, 0.3],
        [G, 0.2, 0.2],
        [F, 0.1, 0.15],
        [C, 0.2, 0.2],
        
        [G, 0.1, 0.1],
        [G, 0.1, 0.1],
        [A2, 0.1, 0.1],
        [F, 0.2, 0.2],

        [D, 0.1, 0.1],
        [D, 0.2, 0.15],
        [G, 0.1, 0.1],
        [G, 0.1, 0.1],
        [A2, 0.2, 0.2],
        [F, 0.2, 0.2],
        
        [D, 0.2, 0.2],
        [E, 0.1, 0.1],
        [F, 0.1, 0.1],
        [E, 0.1, 0.1],
        [D, 0.2, 0.1],
]

    for note, delay1, delay2 in notes:                
        playtone(note,volume,delay1,delay2)
        

    # Set PWM duty (volume off)
    buzzer.duty_u16(0)
        
while True: # Run forever
    
    time.sleep(0.01) # Delay to stop unnecessary program speed
    
    if pir.value() == 1: # If PIR detects movement
        
        print("I SEE YOU!")
    
        alarm() # Call our function
        
        print("Sensor active") # Let us know that the sensor is active again

