"""
* 프로젝트명 : 2023 SMESPC TurtleKeyboardEventProcessing
* 프로그램의 목적 및 기본 기능 :
* -TurtleKeyboardEventProcessing
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
import turtle

screen = turtle.Screen()
screen.screensize(500, 500, 'light green')
turtle.setup(500, 500)
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.shapesize(5)


def turn_left_90():
    t.left(90)


def turn_right_90():
    t.right(90)


def forward_10():
    t.forward(10)


def backward_10():
    t.backward(10)


def main():
    screen.onkey(turn_left_90, "Up")
    screen.onkey(turn_right_90, "Down")
    screen.onkey(forward_10, "Right")
    screen.onkey(backward_10, "Left")

    screen.listen()
    screen.mainloop()


if __name__ == "__main__":
    main()
