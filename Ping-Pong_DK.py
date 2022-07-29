import turtle
from random import choice, randint


window = turtle.Screen()
window.title('Ping-Pong_DK')
window.setup(700,500)
window.tracer(2)

bord = turtle.Turtle()
bord.hideturtle()
bord.speed(0)
bord.color('green')
bord.begin_fill()
bord.up()
bord.goto(-300,200)
bord.down()
bord.goto(-300,-200)
bord.goto(300,-200)
bord.goto(300,200)
bord.goto(-300,200)
bord.end_fill()


bord.goto(0,200)
bord.color('white')
bord.pensize(3)
bord.setheading(270)
for i in range(1,48):
    if i%2 == 0:
        bord.up()
        bord.forward(8)
        bord.down()
    else:
        bord.forward(9)


rocka = turtle.Turtle()
rocka.up()
rocka.color('white')
rocka.shape('square')
rocka.shapesize(3,0.5)
rocka.goto(-280,0)

rockb = turtle.Turtle()
rockb.up()
rockb.color('white')
rockb.shape('square')
rockb.shapesize(3,0.5)
rockb.goto(280,0)

counta = 0

FONT = ('Arial',32)
scorea = turtle.Turtle()
scorea.speed(0)
scorea.hideturtle()
scorea.up()
scorea.setposition(-100,195)
scorea.write(counta, font=FONT)

countb = 0

FONT = ('Arial',32)
scoreb = turtle.Turtle()
scoreb.speed(0)
scoreb.hideturtle()
scoreb.up()
scoreb.setposition(100,195)
scoreb.write(countb, font=FONT)

def move_upa():
    y = rocka.ycor() + 10
    if y > 170:
        y = 170
    rocka.sety(y)

def move_downa():
    y = rocka.ycor() - 10
    if y < -170:
        y = -170
    rocka.sety(y)
    
def move_upb():
    y = rockb.ycor() + 10
    if y > 170:
        y = 170
    rockb.sety(y)

def move_downb():
    y = rockb.ycor() - 10
    if y < -170:
        y = -170
    rockb.sety(y)
    

window.listen()

window.onkeypress(move_upa, 'q')
window.onkeypress(move_downa, 'a')

window.onkeypress(move_upb, 'p')
window.onkeypress(move_downb, 'l')


ball = turtle.Turtle()
ball.speed(0)
ball.color('white')
ball.shape('circle')
ball.shapesize(0.5)
ball.up()

dx = 0.2
dy = -0.3

while True:
    window.update()

    ball.setx(ball.xcor() +  dx)
    ball.sety(ball.ycor() +  dy)
    
    if ball.ycor() >= 195:
        dy = -dy
        
    if ball.ycor() <= -195:
         dy = - dy
    
    if ball.xcor() >= 295:
        countb +=1
        scoreb.clear()
        scoreb.write(countb, font=FONT)
        
        ball.goto(0,randint(-150,150))
        dx = choice([-0.2,0.2])
        dy = choice([-0.3,0.3])

    if ball.xcor() <= -295:
        counta +=1
        scorea.clear()
        scorea.write(counta, font=FONT)
        
        ball.goto(0,randint(-150,150))
        dx = choice([-0.2,0.2])
        dy = choice([-0.3,0.3])
        

    if ball.ycor() >= rocka.ycor()-16 and ball.ycor() <= rocka.ycor()+16 \
   and ball.xcor() >=rocka.xcor()-10.5 and ball.xcor() <=rocka.xcor()+10.5:
        dx = -dx

    if ball.ycor() >= rockb.ycor()-16 and ball.ycor() <= rockb.ycor()+16 \
   and ball.xcor() >=rockb.xcor()-10.5 and ball.xcor() <=rockb.xcor()+10.5:
        dx = -dx


window.mainloop()
