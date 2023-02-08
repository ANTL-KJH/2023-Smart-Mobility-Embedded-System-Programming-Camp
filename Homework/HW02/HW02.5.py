"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW02.5
* 프로그램의 목적 및 기본 기능 :
* -Draw Polygons with User input data
* 프로그램 작성자 : 김재현(2191283)
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""
import turtle, math


def main():
    vertices, side_length, x0, y0 = map(int, input(
        "Input number of vertices polygon, side_length,center position x0 and y0 in one line (e.g., 7 100 100) = ").split())
    print("Drawing a polygon with {} vertices and length ({}) at ({}, {}) ...".format(vertices, side_length, x0, y0))
    t = turtle.Turtle()
    t.color("blue")
    t.dot();    t.write(t.pos())
    t.up();    t.goto(x0, y0);    t.down()
    t.dot();    t.write(t.pos())
    t.up();
    t.goto(x0, y0 + math.sqrt((side_length * side_length / 4) * (
            1 + (math.tan(math.radians(90 - (180 / vertices))) * math.tan(math.radians(90 - (180 / vertices)))))))
    t.down();    t.color("red");
    t.pensize(3)
    t.right(90 - ((180 - (360 / vertices)) / 2))
    for i in range(vertices):
        t.forward(side_length)
        t.dot();        t.write(t.pos())
        t.right(360 / vertices)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
