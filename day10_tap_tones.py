# Imports
from machine import Pin
import time
import tone

song = [
    tone.C,
    tone.C,
    tone.C,
    tone.C,
    tone.F,
    tone.F,
    tone.F,
    tone.E,
    tone.F,
    tone.G,
    tone.A2,
    tone.As2,
    tone.G,
    tone.A2,
    tone.As2,
    tone.C2,
    tone.D2,
    tone.As2,
    tone.A2,
    tone.F,
    tone.G,
    tone.F
]

current_note = 0
# Set up our beam pin
beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True: # Run forever
    
    time.sleep(0.1) # Short delay
    
    if beam.value() == 0: # If the beam is broken
        
        print("1")
        tone.play(song[current_note], 10000, 0.1, 0)
        current_note += 1
        if current_note >= len(song):
            current_note = 0
        
    else:
        
        print("0")
