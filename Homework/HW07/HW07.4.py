"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.4
* 프로그램의 목적 및 기본 기능 :
* -Time data processing with class
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""


class Time:
    def __init__(self, hr, mn, sec):
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__eq__(other):
            return False
        elif (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second):
            return True
        else:
            return False

    def __str__(self):
        s = "({:2}:{:2}:{:2})".format(self.hour, self.minute, self.second)
        return s

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setHour(self, h):
        if h >= 0 and h <= 23:
            self.hour = h

    def setMinute(self, m):
        if m >= 0 and m <= 59:
            self.minute = m

    def setSecond(self, s):
        if s >= 0 and s <= 59:
            self.second = s


def main():
    times = [
        Time(23, 59, 59),
        Time(9, 0, 5),
        Time(13, 30, 0),
        Time(3, 59, 59),
        Time(0, 0, 0),
    ]
    print("times before sorting : ")
    for t in times:
        print(t)
    #
    times.sort()
    print("\ntimes after sorting : ")
    for t in times:
        print(t)


if __name__ == "__main__":
    main()
