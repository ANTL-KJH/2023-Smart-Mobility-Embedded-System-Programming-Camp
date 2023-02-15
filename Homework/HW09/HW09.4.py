"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW09.4
* 프로그램의 목적 및 기본 기능 :
* -Simple StopWatch with Tkinter
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
import time
from tkinter import *

class StopWatch():
    def __init__(self, window):
        self.window = window
        self.frame = LabelFrame(window, text="My Simple Stop Watch", relief=GROOVE)
        self.frame.grid(row=0, column=0)
        self.start_time = time.time()
        self.stop_time = time.time()
        self.elapsed_time = 0.0
        self.prev_elapsed_time = 0.0
        self.running = False
        self.timeText = Label(self.frame, height = 5, text="{:>7s}".format("0.000"), font=("Arial 40 bold"))
        self.timeText.pack(side = TOP)
        self.startButton = Button(self.frame, width=10, text="Start", bg="green", command=self.start)
        self.startButton.pack(side = LEFT)
        self.stopButton = Button(self.frame, width=10, text="Stop", bg="red", command=self.stop)
        self.stopButton.pack(side = LEFT)
        self.resetButton = Button(self.frame, width=10, text="Reset", bg="yellow", command=self.reset)
        self.resetButton.pack(side = LEFT)

    def runTimer(self):
        if(self.running):
            self.cur_time = time.time()
            time_diff = self.cur_time - self.start_time
            self.elapsed_time = time_diff + self.prev_elapsed_time
            self.timeText.configure(text="{:7.3f}".format(self.elapsed_time))
        self.window.after(10, self.runTimer)

    def start(self):
        if(self.running != True):
            self.running = True
            self.start_time = time.time()
            self.elapsed_time = self.elapsed_time

    def stop(self):
        self.running = False
        self.prev_elapsed_time = self.elapsed_time

    def reset(self):
        self.running = False
        self.elapsed_time = 0.0
        self.prev_elapsed_time = 0.0
        self.timeText.configure(text="{:>7s}".format("0.000"))

def main():
    window = Tk()
    window.title("My Simple Stop Watch")
    stop_watch = StopWatch(window)
    stop_watch.runTimer()
    window.mainloop()

if __name__ == "__main__":
    main()