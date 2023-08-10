import turtle
import time
import random

delay = 0.08

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Yoriyoi hebigēmu")
wn.setup(width=600, height=600)
wn.tracer(0)
player = turtle.Turtle()
player.penup()
player.shape("square")
player.color("#cccf7a")
# lol.fd(34)

player.hideturtle()

# block1 = turtle.Turtle()
# block1.shape("square")
# block1.shapesize(12,12,1)
# snake head
head = turtle.Turtle()
head.shape("square")
head.color("#cbd10d")
head.penup()
# head.goto(20, 20)
head.direction = "right"
# head.shapesize(0.5,0.5,1)
head.speed(1)
# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
# food.shapesize(0.5,0.5,1)
# food.color("#b52f18")
food.penup()
food.goto(0, 100)

segments = []
for segment in segments:
    player.goto(260, 0)
    player.write("Immanuel", align="center", font=("algerian", 24, "normal"))
    player.goto(0, -260)
    player.write("Bacchus", align="center", font=("algerian", 24, "normal"))

fo_col = random.randint(1, 4)


def bgcol1():
    wn.bgcolor("#157321")
    food.color("#157321")


def bgcol2():
    wn.bgcolor("#732615")
    food.color("#732615")


def bgcol3():
    wn.bgcolor("#888a29")
    food.color("#888a29")


def bgcol4():
    wn.bgcolor("#1b3869")
    food.color("#1b3869")


# scoreboards
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0  High score: 0", align="center", font=("ds-digital", 24, "bold"))


# Functions
def go_up():
    bgcol1()
    if head.direction != "down":
        head.direction = "up"


def go_down():
    bgcol2()
    if head.direction != "up":
        head.direction = "down"


def go_left():
    bgcol3()
    if head.direction != "right":
        head.direction = "left"


def go_right():
    bgcol4()
    if head.direction != "left":
        head.direction = "right"


def move():
    # head.direction = "up"
    if head.direction == "up":
        y = head.ycor()
        y = y + 20
        head.sety(y)

    if head.direction == "down":
        y = head.ycor()
        y = y - 20
        head.sety(y)
    if head.direction == "left":
        x = head.xcor()
        x = x - 20
        head.setx(x)
    if head.direction == "right":
        x = 0
        x = head.xcor()
        head.setx(x + 20)


# keyboard bindings
wn.listen()

wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
imm = 1

while True:
    wn.update()

    print(head.direction)

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.4)
        head.goto(0, 0)
        x, y = random.randint(100,100), random.randint(100,100)
        food.goto(x,y)

        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0

        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("ds-digital", 24, "normal"))

    if head.distance(food) < 20:

        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        player.goto(y, x)
        imm = str(imm)
        player.write(imm, align="center", font=("algerian", 13, "normal"))
        food.goto(x, y)
        imm = int(imm)
        imm += 1


        # lol.color("yellow")
        player.goto(y, x)
        #player.write(imm, align="center", font=("algerian", 13, "normal"))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#a2a832")
        new_segment.shapesize(0.5, 0.5, 1)
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 1

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                 font=("ds-digital", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        print(index)
        print(index - 1)
        xx = segments[index - 1].xcor()
        yy = segments[index - 1].ycor()
        segments[index].goto(xx, yy)
    if len(segments) > 0:
        xx = head.xcor()
        yy = head.ycor()
        segments[0].goto(xx, yy)

    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1

            sc.clear()
            sc.write("score: {}  High score: {}".format(score, high_score), align="center",
                     font=("ds-digital", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
