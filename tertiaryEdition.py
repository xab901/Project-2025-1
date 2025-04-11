from gpiozero import LED, Button
from time import sleep, time
from random import uniform
from signal import pause

led = LED(4)  # set up the pin as output
right_button = Button(17)
left_button = Button(14)

left_name = input('left player name is: ')
right_name = input('right player name is: ')

# 初始化玩家分数
left_score = 0
right_score = 0

while True:
    led.on()
    sleep(uniform(5, 10))  # randomize sleep time
    # 记录 LED 熄灭的时间
    led_off_time = time()
    led.off()

    def pressed(button):
        nonlocal left_score, right_score, led_off_time
        # 记录玩家按下按钮的时间
        press_time = time()
        # 计算玩家反应时间
        reaction_time = press_time - led_off_time

        # show which pin button was on
        if button.pin.number == 14:
            left_score = left_score + 1
            print(left_name + ' won the game')
        else:
            right_score = right_score + 1
            print(right_name + ' won the game')

        # 显示当前玩家总分数
        print(f"{left_name}'s total score: {left_score}")
        print(f"{right_name}'s total score: {right_score}")
        # 显示玩家反应时间
        print(f"Reaction time: {reaction_time:.3f} seconds")

    right_button.when_pressed = pressed
    left_button.when_pressed = pressed

    # 等待按钮被按下
    while not (right_button.is_pressed or left_button.is_pressed):
        pass

    # 重置按钮事件处理函数，避免重复触发
    right_button.when_pressed = None
    left_button.when_pressed = None

    # 给玩家一些时间查看结果
    sleep(2)
    
