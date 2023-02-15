"""
* 프로젝트명 : 2023 SMESPC TurtleMouseEventProcessing
* 프로그램의 목적 및 기본 기능 :
* -TurtleMouseEventProcessing
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
import turtle

board = turtle.Screen()
board.screensize(800, 600, 'light blue')
pointer = turtle.Turtle()
pointer.color('red')
pointer.pencolor('red')
pointer.ht()


def teleport_btn1(x, y):
    pointer.pencolor('red')
    pointer.goto(x, y)
    pointer.dot(10, "red")
    pointer.write((pointer.xcor(), pointer.ycor()))


def teleport_btn3(x, y):
    pointer.pencolor('blue')
    pointer.goto(x, y)
    pointer.dot(10, "blue")
    pointer.write((pointer.xcor(), pointer.ycor()))


def quitThis():
    board.bye()


def main():
    pointer.write((pointer.xcor(), pointer.ycor()))
    board.onclick(teleport_btn1, btn=1)
    board.onclick(teleport_btn3, btn=3)
    board.onkey(quitThis, 'q')
    board.listen()
    board.mainloop()

if __name__ == "__main__":
    main()
