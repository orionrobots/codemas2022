# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create our library of tone variables

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
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)
    
# Play the tune
playtone(G, volume, 0.2, 0.3)
playtone(G, volume, 0.2, 0.2)
playtone(F, volume, 0.1, 0.15)
playtone(C, volume, 0.2, 0.2)

playtone(G, volume, 0.1, 0.1)
playtone(G, volume, 0.1, 0.1)
playtone(A2, volume, 0.1, 0.1)
playtone(F, volume, 0.2, 0.2)



# Duty to 0 to turn the buzzer off
buzzer.duty_u16(0)

