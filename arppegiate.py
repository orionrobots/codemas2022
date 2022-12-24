import time
import tone

volume = 10000

def arpeggiate(notes, count, start_vol, end_vol):
    vol_step = int((end_vol - start_vol) / count)
    vol = start_vol
    for n in range(count):
        for note in notes:
            tone.play(note, vol, 0.02, 0)
        vol += vol_step


arpeggiate([tone.C0, tone.C, tone.C2], 20, 10000, 0)
arpeggiate([tone.E0, tone.E, tone.E2], 20, 10000, 0)
arpeggiate([tone.A0, tone.A, tone.A2], 20, 10000, 0)
time.sleep(0.2)
arpeggiate([tone.C, tone.Ds, tone.G], 10, 0, 10000)
arpeggiate([tone.C, tone.Ds, tone.G], 10, 10000, 0)
arpeggiate([tone.A, tone.C, tone.E], 10, 0, 10000,)
arpeggiate([tone.A, tone.C, tone.E], 10, 10000, 0)
arpeggiate([tone.C, tone.Ds, tone.G], 10, 0, 10000)
arpeggiate([tone.C, tone.Ds, tone.G], 10, 10000, 0)
arpeggiate([tone.F0, tone.Gs0, tone.C], 10, 0, 10000)
arpeggiate([tone.F0, tone.Gs0, tone.C], 5, 10000, 5000)
arpeggiate([tone.F0, tone.Gs0, tone.C], 5, 5000, 7500)
arpeggiate([tone.F0, tone.Gs0, tone.C], 5, 5000, 800)
arpeggiate([tone.F0, tone.Gs0, tone.C], 5, 800, 5000)
arpeggiate([tone.F0, tone.Gs0, tone.C], 5, 5000, 0)
