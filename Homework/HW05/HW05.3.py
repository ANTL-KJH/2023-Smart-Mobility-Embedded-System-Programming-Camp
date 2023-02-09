"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW05.3
* 프로그램의 목적 및 기본 기능 :
* -Draw Polygons with Turtle Graphics
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import turtle, math


def drawPolygon(t, tu):
    vertices = tu[0]
    sidelen = tu[1]
    px = tu[2]
    py = tu[3]
    pcolor = tu[4]

    t.up()
    t.goto(px, py)
    t.dot(10, "red")
    t.write(t.pos())
    t.goto(px - (sidelen / 2), py - (sidelen / 2) * (math.tan(math.radians(90 - 180 / vertices))))
    t.dot(10, "blue")
    t.write(t.pos())
    t.pencolor(pcolor)

    t.down()
    for i in range(vertices):
        t.forward(sidelen)
        t.left(360 / vertices)


def main():
    L_polygons = [(3, 100, -250, 100, "red"), (4, 100, 0, 100, "green"), (5, 100, 250, 100, "blue"),
                  (6, 100, -250, -100, "magenta"), (7, 100, 0, -100, "black"), (8, 100, 250, -100, "orange")]
    t = turtle.Turtle()
    for i in range(len(L_polygons)):
        drawPolygon(t, L_polygons[i])
    turtle.title("Drawing polygons with turtle")

    turtle.exitonclick()


if __name__ == "__main__":
    main()
