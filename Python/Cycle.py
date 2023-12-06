import time
import board
import neopixel

NumOfPixels = 150
SleepTime = .001

Pix = {}

for i in range(NumOfPixels):
    Pix[i] = 0,0,0

print(Pix)
