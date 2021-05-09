#1 завдання
import random
number = random.randrange(0,101)
print(number)

#2 завдання
numb = int(input("Введіть рандомне число від 0 до 10: "))
numb2 = random.randrange(0,11)
print("Випадає число: " ,numb2)
if numb == numb2:
    print("Ти вийграв!!!")
else:
    print("Ти програв =(")

#3 завдання
pryclad = 100 - 50
print(pryclad)
modul = print(abs(pryclad))

if modul > 0:
    print("Число додатне")
else:
    print("Завдання зроблено неправильно")

#4 задача
from random import choice, random
from turtle import *
from freegames import vector

def value():
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

# початкові координати появи м'яча
ball = vector(5, 0)
# м'яч має рандомний напрямок, який генерується з функції value
aim = vector(value(), value())
state = {1: 0, 2: 0}

def move(player, change):
    "Move player position by change."
    state[player] += change

def rectangle(x, y, width, height):
    "Draw rectangle at (x, y) with given width and height."
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    # розмір м'яча
    dot(20)
    update()
    # границі
    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return
    # швидкість руху м'яча
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# клавіші управління
onkey(lambda: move(1, 30), 'w')
onkey(lambda: move(1, -30), 's')
onkey(lambda: move(1, -15), 'd')
onkey(lambda: move(1, 15), 'a')
onkey(lambda: move(2, 30), '8')
onkey(lambda: move(2, -30), '5')
onkey(lambda: move(2, -15), '6')
onkey(lambda: move(2, 15), '4')
draw()
done()

#5 задача
from turtle import *
from freegames import square, vector

# перший гравець
# початкова точка
p1xy = vector(-10, 0)
# напрямок
p1aim = vector(4, 0)
p1body = set()

# другий гравець
# початкова точка
p2xy = vector(100, 0)
# напрямок
p2aim = vector(-4, 0)
p2body = set()

# перший гравець
# початкова точка
p3xy = vector(0, 10)
# напрямок
p3aim = vector(0, 4)
p3body = set()

# чи ми знаходимся в межах карти
def inside(head):
    "Return True if head inside screen."
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    "Advance players and draw game."
    # рух гравця 1
    p1xy.move(p1aim)
    p1head = p1xy.copy()
    
    # рух гравця 2
    p2xy.move(p2aim)
    p2head = p2xy.copy()
    
    # рух гравця 3
    p3xy.move(p3aim)
    p3head = p3xy.copy()


    # перевірка чи гравець 1 врізався в гравця 2
    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    # перевірка чи гравець 2 врізався в гравця 1
    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    # збільшення тіла гравця 1
    p1body.add(p1head)
    # збільшення тіла гравця 2
    p2body.add(p2head)
    # збільшення тіла гравця 3
    p3body.add(p3head)

    # вигляд обох гравців, цифра 3 означає розмір, а колір можна міняти
    square(p1xy.x, p1xy.y, 3, 'yellow')
    square(p2xy.x, p2xy.y, 3, 'blue')
    square(p3xy.x, p3xy.y, 3, 'black')
    update()
    # швидкість руху гравців
    ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), '4')
onkey(lambda: p2aim.rotate(-90), '6')
onkey(lambda: p3aim.rotate(90), 'g')
onkey(lambda: p2aim.rotate(-90), 'j')
draw()
done()

#7 - 10 завдання

import random
from random import choice
from turtle import *
from freegames import floor, vector

# рахунок
state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
# напрямок
aim = vector(5, 0)
# початкові координати пекмена
pacman = vector(-40, -80)
# вороги
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
    [vector(-180, 160), vector(5, 0)],
]

def random():
    return random.randrange(0,2)

# карта, 0 - це стіна, 1 - це дорога
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, random(), 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 1, random(), 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, random(), 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 1, random(), 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 0, 1, random(), 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, random(), 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0,
    0, 1, 0, random(), 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, random(), 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, random(), 0, 1, 0,
    0, 0, 0, 0, 1, random(), 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, random(), 0,
    0, 1, 0, random(), 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, random(), 1, 1, 0, 1, 1, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, random(), 1, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, random(), 0, 1, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, random(), 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, random(), 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, random(), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                # розмір їжі та її колір
                path.dot(2, 'yellow')

def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    # розмір пекмена та його колір
    dot(20, 'red')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        # розмір ворогів та їх колір
        dot(20, 'white')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()