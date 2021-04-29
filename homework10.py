#змійка
# підключаємо бібліотеки 
from turtle import * # черепашка
from random import randrange # рандом
from freegames import square, vector # freegames - вектори

food = vector(10, 10) # 0, 0 початкові координати
snake = [vector(0, 0)] # 10, 0 початкові координати змійки
aim = vector(0, 10) # 0, -10 початковий напрям змійки

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    # Перевірка на те чи ми знаходимось всередині карти
    # Границі карти в пікселях, можна міняти
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    # рух змійки
    head = snake[-1].copy()
    head.move(aim)
    # Створюємо червоний квадрат перед змійкою, якщо вона вилазить за межі карти
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'black')
        update()
        return

    snake.append(head)
    
    # рандомна поява їжі
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    # колір змійки 
    
    for body in snake:
        square(body.x, body.y, 9, 'pink')
    
    # колір їжі
    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)
# початковий розмір екрану
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# клавіші управління, можна міняти
onkey(lambda: change(10, 0), 'Right') # d
onkey(lambda: change(-10, 0), 'Left') # a
onkey(lambda: change(0, 10), 'Up') # w
onkey(lambda: change(0, -10), 'Down') # s
move()
done()
#пробачте я не зрозумів як поміняти колір заднього фону

#флеппі бьорд

"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import * # рандомні числа (випадкові числа)
from turtle import *  # бібліотека для графіки
from freegames import vector # додаткова бібліотека для turtle

bird = vector(0, 0) # птах
balls = [] # це м'ячі
# функція для нажимання на екран, підстрибування
def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 50) # 0,30 це відстань на яку ми підстрибуємо
    bird.move(up)
# перевірка на те чи ми заходимо за межі карти
def inside(point):
    "Return True if point on screen."
    return -300 < point.x < 300 and -300 < point.y < 300
# для малювання кольорів і графіки
def draw(alive):
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)
# якщо ми живі то світимося зеленим кольором
    if alive:
        dot(10, 'violet')
    else:
        dot(10, 'black') # якщо помираємо світимося червоним кольором
# м'ячі позначені чорним кольором
    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'green')

    update()

def move():
    "Update object positions."
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()