import turtle
import time
import random

speed = 0.20

# Snake game window
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('orange')
window.setup(width=600, height=600)
window.tracer(0)


# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white') 
head.penup()
head.goto(0, 100)
head.direction = 'stop'


# Eat
eat = turtle.Turtle()
eat.speed(0)
eat.shape('circle')
eat.color('red')
eat.penup()
eat.goto(0, 0)
eat.shapesize(0.80, 0.80)

# Tail
tails = []

# Snake Movee
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


# Move Key Set
def goUp():
    if head.direction != 'down':
        head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'
       
def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'


# Move Key
window.listen()
window.onkey(goUp, 'Up')
window.onkey(goDown, 'Down')
window.onkey(goRight, 'Right')
window.onkey(goLeft, 'Left')


while True:
    window.update()


    if head.distance(eat) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        eat.goto(x, y)


        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('brown')
        newTail.penup()
        tails.append(newTail)


    for i in range(len(tails) -1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)


    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()
    time.sleep(speed) 