from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

count = 0

while(True):
    if(count == 5):
        sense_hat.clear()
        break

    sense.show_message("SEND NUDES", text_colour=[255, 0, 0], back_colour=[100, 100, 100])
    count = count + 1