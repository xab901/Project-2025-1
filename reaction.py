from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4) # set up the pin as output
led.on()
sleep(uniform(5,10)) # randomize sleep time
led.off()
