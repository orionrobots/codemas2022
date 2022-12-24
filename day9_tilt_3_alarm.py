# Imports
from machine import Pin
import time
import tone

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up a counter variable at zero
tiltcount = 0

# Create a state variable at zero
state = 0

volume = 1000

def alarm():
    notes = [
            (tone.G, 0.3, 0.3),
            (tone.A2, 0.2, 0.3),
            (tone.D, 0.2, 0.3),
            (tone.A2, 0.3, 0.3),
            (tone.B2, 0.4, 0.3),

            (tone.D2, 0.1, 0.1),
            (tone.C2, 0.1, 0.1),
            (tone.B2, 0.1, 0.1),
            (tone.G, 0.2, 0.3),
            
    ]
    for note, delay1, delay2 in notes:
        tone.play(note, volume, delay1, delay2)

while True: # Run forever
    
    time.sleep(0.1) # Short delay
        
    if state == 0 and tilt.value() == 1: # If state is 0 and our pin is HIGH
                    
         tiltcount = tiltcount + 1 # Add +1 to tiltcount
            
         state = 1 # Change state to 1

         print("tilts =",tiltcount) # Print our new tiltcount
         
         if tiltcount == 3:
             alarm()
    if state == 1 and tilt.value() == 0: # If state is 1 and our pin is LOW
                            
        state = 0 # Change the state to 0

