"""
* 프로젝트명 : 2023 SMESPC Temperature Converter
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

from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='deg C').grid(row=0, column=0)
        self.c_var = DoubleVar()
        Entry(frame, textvariable=self.c_var).grid(row=0, column=1)
        self.f_var = DoubleVar()
        Entry(frame, textvariable=self.f_var).grid(row=1, column=1)
        button_CF = Button(frame, text='deg C -> deg F Convert', bg="orange", command=self.convert_CF)
        button_CF.grid(row=2, columnspan=2)
        button_FC = Button(frame, text='deg F -> deg C Convert', bg="lime", command=self.convert_FC)
        button_FC.grid(row=3, columnspan=2)

    def convert_CF(self):
        c = self.c_var.get()
        f = c * 1.8 + 32
        f_round = round(f, 3)
        self.f_var.set(f_round)

    def convert_FC(self):
        f = self.f_var.get()
        c = (f - 32) / 1.8
        c_round = round(c, 3)
        self.c_var.set(c_round)


def main():
    root = Tk()
    root.wm_title("Temp Converter")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
