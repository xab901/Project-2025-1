from gpiozero import LED, Button
from time import sleep

led = LED(4) # set up the pin as output
led.on()
sleep(5)
led.off()
