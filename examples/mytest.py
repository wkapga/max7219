#!/usr/bin/env python

import max7219.led as led
import max7219.canvas as canvas
import max7219.transitions as transitions
import time
from random import randrange

led.init()
#led.show_message("Heyy!", transition = transitions.left_scroll)

#led.show_message("Heyy!", transition = transitions.up_scroll)
#for x in range(256):
#    led.letter(x)
#    time.sleep(0.1)

while True:
    for x in range(200):
#       canvas.set_on( randrange(4),1)       
        canvas.set_on(x % 8 , 1)

#        canvas.set_on(sin((x*100) % 8 , 1)
        canvas.scroll(2)
        canvas.render()
        time.sleep(0.1)
#    canvas.clear()

#    for x in range(500):
#        canvas.set_off(randrange(8), randrange(8))
#        canvas.scroll(randrange(16))
#        canvas.render()
#        time.sleep(0.01)

#    for x in range(500):
#        canvas.set_on(4, 4)
#        canvas.scroll(randrange(8))
#        canvas.render()
#        time.sleep(0.01)
