from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('left player name is: ')
right_name = input('right player name is: ')

# 初始化玩家分数
left_score = 0
right_score = 0

while True:
    led.on()
    sleep(uniform(5, 10))
    # 记录 LED 熄灭的时间
    start_time = time()
    led.off()

    def pressed(button):
        global left_score, right_score
        # 计算反应时间
        reaction_time = time() - start_time
        if button.pin.number == 14:
            print(f"{left_name} won the game")
            left_score += 1
        else:
            print(f"{right_name} won the game")
            right_score += 1
        right_button.when_pressed = None
        left_button.when_pressed = None
        # 显示玩家总分数和反应时间
        print(f"{left_name}'s total score: {left_score}")
        print(f"{right_name}'s total score: {right_score}")
        print(f"Reaction time: {reaction_time:.3f} seconds")
        sleep(2)

    right_button.when_pressed = pressed
    left_button.when_pressed = pressed

    while not (right_button.is_pressed or left_button.is_pressed):
        sleep(0.1)

led.close()
right_button.close()
left_button.close()
    
