import time
import random
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 12)

while True:
    for i in range(12):
        pv = (random.randrange(255)) #PixelValue
        vt = {
        1:(pv,0,0),
        2:(0,pv,0),
        3:(0,0,pv)
        } #ValueTable
        choice = random.choice(list(vt.keys()))
        pixels[i] = vt[choice]
        time.sleep(.05)
