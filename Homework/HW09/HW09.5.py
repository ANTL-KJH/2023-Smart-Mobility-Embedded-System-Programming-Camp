"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW09.5
* 프로그램의 목적 및 기본 기능 :
* -Bouncing ball based on Tkinter keyboard event
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.10
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.10	v1.0	최초 작성
"""

from tkinter import *


def init():
    global window, canvas, DX, DY
    window = Tk()
    window.title("tkinter animation - bouncing ball")
    canvas = Canvas(window, width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(0, 0, 80, 80, fill="red", tags="myBall")
    DX = 1  # DX = 5
    DY = 1  # DY = 5
    print("Initial ball movement")

def keyinput(e):
    key = e.keysym
    global DX, DY
    if key == "Left":
        DX = -1
        DY = 0
    elif key == "Right":
        DX = 1
        DY = 0
    elif key == "Down":
        DX = 0
        DY = 1
    elif key == "Up":
        DX = 0
        DY = -1
    elif key == "Escape":
        DX = 1
        DY = 1

def animate():
    global DX, DY
    canvas.move("myBall", DX, DY)
    pos = canvas.coords("myBall")
    #print("coords of Ball : {}, {}, {}, {}".format(pos[0], pos[1], pos[2], pos[3]))
    window.bind("<Key>", keyinput)
    if pos[0] <= 0:
        print("bounced by left board ")
        DX *= -1
    if pos[2] >= canvas.winfo_width():
        print("bounced by right board")
        DX *= -1
    if pos[1] <= 0:
        print("bounced by ceil board")
        DY *= -1
    if pos[3] >= canvas.winfo_height():
        print("bounced by bottom board")
        DY *= -1
    canvas.update_idletasks()
    canvas.update()
    canvas.after(50, animate)

def main():
    init()
    animate()
    mainloop()


if __name__ == "__main__":
    main()
