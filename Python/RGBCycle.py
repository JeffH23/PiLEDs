import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 12)
SleepTime=.001
r = 0
g = 0
b = 255
while True:
    print((r,g,b))
    for i in range(255):
        pixels.fill((r,g,b))
        r=r+1
        b=b-1
        print((r,g,b))
        time.sleep(SleepTime)
    print((r,g,b))
    for i in range(255):
        pixels.fill((r,g,b))
        g=g+1
        r=r-1
        print((r,g,b))
        time.sleep(SleepTime)
    print((r,g,b))
    for i in range(255):
        pixels.fill((r,b,g))
        b=b+1
        g=g-1
        print((r,g,b))
        time.sleep(SleepTime)