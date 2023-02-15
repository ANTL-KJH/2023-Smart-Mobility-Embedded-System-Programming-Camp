"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW09.2
* 프로그램의 목적 및 기본 기능 :
* -Bouncing ball based on Turtle graphics keyboard event
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.10
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.10	v1.0	최초 작성
* JH KIM            2023.02.15  v1.1    Keyboard Event Processing
"""
import turtle
import time
from turtle import *

DX = 1
DY = -1
PX = -270
PY = 153


def move_obj(ball):
    global PX, PY, DX, DY
    if PX > 195:
        DX *= -1
        print("Ball Bounced at right wall")
    if PX < -270:
        DX *= -1
        print("Ball Bounced at left wall")
    if PY > 153:
        DY *= -1
        print("Ball Bounced at ceil")
    if  PY < -215:
        DY *= -1
        print("Ball Bounced at bottom")
    PX += DX
    PY += DY
    ball.goto(PX, PY)
    ball.fillcolor('red')
    ball.begin_fill()
    ball.circle(radius=50)
    ball.end_fill()
    time.sleep(0.01)



def Up_Key():
    global DX, DY
    DX = 0
    DY = 1


def Down_Key():
    global DX, DY
    DX = 0
    DY = -1

def Right_Key():
    global DX, DY
    DX = 1
    DY = 0

def Left_Key():
    global DX, DY
    DX = -1
    DY = 0

def Esc_Key():
    global DX, DY
    DX = -1
    DY = -1

def main():
    screen = turtle.Screen()
    screen.screensize(600, 500)
    turtle.setup(600, 500)
    ball = turtle.Turtle()

    ball.hideturtle()
    ball.color("red")
    ball.penup()
    ball.goto(-300, 200)
    ball.speed(0)
    ball.right(45)
    ball.pendown()
    screen.tracer(False)
    while True:
        # clearing the turtle work
        ball.clear()
        screen.onkey(Up_Key, "Up")
        screen.onkey(Down_Key, "Down")
        screen.onkey(Right_Key, "Right")
        screen.onkey(Left_Key, "Left")
        screen.onkey(Esc_Key, "Escape")
        screen.listen()
        move_obj(ball)
        screen.update()
        # ball.forward(0.6)


if __name__ == "__main__":
    main()
