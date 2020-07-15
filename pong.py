import turtle

wn = turtle.Screen()
wn.title("Pong by @emilstahl97")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#move paddle a up

def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)


#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop 

while True:
    wn.update()
