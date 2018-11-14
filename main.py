from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

while(True):
    sense.show_message("SEND NUDES", text_colour=[255, 0, 0], back_colour=[100, 100, 100])