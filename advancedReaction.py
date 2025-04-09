from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is: ')
right_name = input('right player name is: ')

while True:
    led.on()
    sleep(uniform(5, 10))
    led.off()

    def pressed(button):
        if button.pin.number == 14:
            print(f"{left_name} won the game")
        else:
            print(f"{right_name} won the game")
        right_button.when_pressed = None
        left_button.when_pressed = None
        sleep(2)

    right_button.when_pressed = pressed
    left_button.when_pressed = pressed

    while not (right_button.is_pressed or left_button.is_pressed):
        sleep(0.1)

led.close()
right_button.close()
left_button.close()
    
