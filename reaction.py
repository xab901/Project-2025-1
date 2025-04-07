from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4) # set up the pin as output
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(5,10)) # randomize sleep time
led.off()

def pressed(button):
	# show which pin button was on
	print(str(button.pin.number) + 'won the game')

right_button.when_pressed = pressed
left_button.when_pressed = pressed
