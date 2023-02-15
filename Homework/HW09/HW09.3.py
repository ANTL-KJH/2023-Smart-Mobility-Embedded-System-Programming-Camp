"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW09.3
* 프로그램의 목적 및 기본 기능 :
* -Student Data Input GUI based on Tkinter
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

        Label(frame, text='Name').grid(row=0, column=0)
        self.name = StringVar()
        Entry(frame, textvariable=self.name).grid(row=0, column=1, columnspan=2)

        Label(frame, text='Korean').grid(row=1, column=0)
        self.korean = IntVar()
        Entry(frame, textvariable=self.korean).grid(row=1, column=1, columnspan=2)

        Label(frame, text='English').grid(row=2, column=0)
        self.english = IntVar()
        Entry(frame, textvariable=self.english).grid(row=2, column=1, columnspan=2)

        Label(frame, text='Math').grid(row=3, column=0)
        self.math = IntVar()
        Entry(frame, textvariable=self.math).grid(row=3, column=1, columnspan=2)

        button_Quit = Button(frame, text='Quit', bg="red", command=self.quit)
        button_Quit.grid(row=4, column=0, sticky=NSEW)
        button_Fetch = Button(frame, text='Fetch', bg="green", command=self.fetch)
        button_Fetch.grid(row=4, column=1, columnspan=2, sticky=NSEW)

    def quit(self):
        exit(0)

    def fetch(self):
        n = self.name.get()
        k = self.korean.get()
        e = self.english.get()
        m = self.math.get()

        print("Input data:")
        print("Name:{}".format(n))
        print("Korean:{}".format(k))
        print("English:{}".format(e))
        print("Math:{}".format(m))


def main():
    root = Tk()
    root.wm_title("input Dialog with Label and Entry Objects")
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
