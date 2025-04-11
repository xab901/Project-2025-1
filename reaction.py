from gpiozero import LED, Button
from time import sleep, time
from random import uniform
from signal import pause

led = LED(4) # set up the pin as output
right_button = Button(17)
left_button = Button(14)

left_name = input('Left player name is: ')
right_name = input('Right player name is: ')

# Initialize scores
left_score = 0
right_score = 0
round_count = 0

def start_round():
	global round_count, led_off_time
	round_count += 1

	print(f"\n--- Round {round_count} ---")
	print("Ready...")
	sleep(1)
	led.on()
	print("Go!")
	sleep(uniform(5, 10)) # randomize sleep time
	led.off()
	led_off_time = time() # record when LED turned off

def pressed(button):
	global left_score, right_score

	# Calculate reaction time
	reaction_time = (time() - led_off_time) * 1000 # in milliseconds

	# Determine winner
	if button.pin.number == 14:
		left_score += 1
		winner = left_name
	else:
		right_score += 1
		winner = right_name

	# Display results
	print(f"\n{winner} wins this round!")
	print(f"Reaction time: {reaction_time:.2f} ms")
	print(f"Current scores - {left_name}: {left_score} | {right_name}: {right_score}")

	# Prepare for next round
	sleep(2) # pause before next round
	start_round()

right_button.when_pressed = pressed
left_button.when_pressed = pressed

# Start the first round
print(f"\nGame starting! First to react wins!")
start_round()

pause()
