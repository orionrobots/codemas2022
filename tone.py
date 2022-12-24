# Create our library of tone variables
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

A0 = 440 // 2
As0 = 466 // 2 
B0 = 494 // 2
C0 = 523 // 2
Cs0 = 554 // 2
D0 = 587 // 2
Ds0 = 622 // 2
E0 = 659 // 2
F0 = 698 // 2
Fs0 = 730 // 2
G0 = 784 // 2
Gs0 = 830 // 2


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
C2 = 523 * 2 -20
Cs2 = 554 * 2
D2 = 587 * 2
Ds2 = 622 * 2
E2 = 659 * 2
F2 = 698 * 2
Fs2 = 740 * 2
G2 = 784 * 2
Gs2 = 830 * 2

# Create our function with arguments
def play(note,vol,delay1,delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

