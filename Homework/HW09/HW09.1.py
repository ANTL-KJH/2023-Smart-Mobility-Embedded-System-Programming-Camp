"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW09.1
* 프로그램의 목적 및 기본 기능 :
* -DrawPolygons with Turtle Graphics
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
import turtle, math


def drawCircle(t, center_pos, radius, color):
    px, py = center_pos
    t.up()
    t.pencolor(color)
    t.goto(px, py)
    t.dot(10)
    t.write(t.pos())
    t.goto(px, py - radius)
    t.dot(10)
    t.write(t.pos())
    t.down()
    t.circle(radius)


def drawPolygon(t, center_pos, shape, radius, color):
    px, py = center_pos
    t.up()
    t.pencolor(color)
    t.goto(px, py)
    t.dot(10)
    t.write(t.pos())
    vertices = getnumVertices(shape)
    side_len = radius * math.sin(math.radians(180 / vertices)) * 2
    new_py = py - radius * math.sin(math.radians(90 - 180 / vertices))
    t.goto(px - (side_len / 2), new_py)
    t.dot(10)
    t.write(t.pos())
    t.down()
    for i in range(vertices):
        t.forward(side_len)
        t.left(360 / vertices)


def drawStar(t, center_pos, radius, color):
    px, py = center_pos
    t.up()
    t.pencolor(color)
    t.goto(px, py)
    t.dot(10)
    t.write(t.pos())
    vertices = 5
    t.goto(px, py + radius)
    t.dot(10)
    t.write(t.pos())
    t.down()
    t.right(90 -(180 / 5 / 2))
    side_len = radius * math.sin(math.radians(360 / vertices)) * 2
    for i in range(5):
        t.forward(side_len)
        t.right((360 * 2) / 5)
    t.dot(10)
    t.write(t.pos())
    t.down()


def getnumVertices(name):
    verticesData = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6}
    return int(verticesData[name])


def main():
    L_drawings = [(-200, 100, "triangle", 50, "red"), (0, 100, "square", 50, "green"),
                  (200, 100, "pentagon", 50, "blue"), (-200, -100, "hexagon", 50, "orange"),
                  (0, -100, "circle", 50, "brown"), (200, -100, "star", 50, "magenta")]
    t = turtle.Turtle()
    t.pensize(5)
    for i in range(len(L_drawings)):
        center_pos = (L_drawings[i][0], L_drawings[i][1])
        shape = L_drawings[i][2]
        radius = L_drawings[i][3]
        color = L_drawings[i][4]

        if L_drawings[i][2] == "circle":
            drawCircle(t, center_pos, radius, color)
        elif L_drawings[i][2] == "star":
            drawStar(t, center_pos, radius, color)
        else:
            drawPolygon(t, center_pos, shape, radius, color)

    turtle.exitonclick()


if __name__ == "__main__":
    main()
