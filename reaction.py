from gpiozero import LED, Button
from time import sleep
from random import uniform
from signal import pause

led = LED(4) # set up the pin as output
right_button = Button(17)
left_button = Button(14)

left_name = input('left player name is: ')
right_name = input('right player name is: ')

def start_round():
	led.on()
	sleep(uniform(5, 10))
	led.off()

def pressed(button):
	# show which pin button was on
	if button.pin.number == 14:
		print(left_name + ' won the game')
	else:
		print(right_name + ' won the game')
	print("Let's play another round......")
	sleep(1)
	start_round()

right_button.when_pressed = pressed
left_button.when_pressed = pressed

# Start the first round
start_round()

pause()
