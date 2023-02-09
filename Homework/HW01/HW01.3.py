"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW01.3
* 프로그램의 목적 및 기본 기능 :
* -터틀 그래픽을 이용하여 (0,0)을 기준으로 입력된 크기의 직사각형을 그리는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ===================================QQ===================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""
import turtle

def main():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    t.pencolor("red")
    t.pensize(3)
    width = int(input("width = "))
    length = int(input("length = "))

    print("Drawing a rectangle of width({}), length({}) ....".format(width, length))

    t.up(); t.goto(-width/2, -length/2); t.down()

    t.forward(width); t.left(90)
    t.forward(length); t.left(90)
    t.forward(width); t.left(90)
    t.forward(length); t.left(90)

    t.up(); t.home(); t.down()
    turtle.exitonclick()

if __name__ == "__main__":
    main()