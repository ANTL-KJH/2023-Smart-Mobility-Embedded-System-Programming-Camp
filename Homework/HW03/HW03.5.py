"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW03.5
* 프로그램의 목적 및 기본 기능 :
* - 별의 위치와 크기를 입력받고 주어진 조건에 따라 별을 그리는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""
import turtle, math


def main():
    turtle.setup(500, 500)  # set width and height of canvas
    turtle.title("Drawing a star at given position")
    t = turtle.Turtle()
    t.shape('classic')
    num_vertices = 5
    center_x, center_y = map(int, input("input center_x and center_y : ").split(' '))
    center = (center_x, center_y)
    line_length = int(input("line_length of star : "))
    line_color = input("line_color of star (e.g., red, blue) = ")
    t.pencolor(line_color)
    t.dot(10, "red")
    t.write(t.pos())
    t.up()
    t.goto(center)
    t.down()
    t.dot(10, "blue")
    t.write(center)
    start_x = center_x - line_length / 2
    theta = math.radians(360 / num_vertices)  # convert angle in degree into angle in radian
    h = line_length / (2 * math.tan(theta))
    start_y = center_y + h
    t.width(5)
    t.penup()
    t.goto(start_x, start_y)
    t.dot(10, "blue")
    t.write((start_x, start_y))
    t.pendown()  # pen down to draw
    for i in range(num_vertices):
        t.forward(line_length)
        t.right(2 * 360 / num_vertices)
    t.up()
    t.goto(center)
    t.down()
    turtle.exitonclick()


if __name__ == "__main__":
    main()
