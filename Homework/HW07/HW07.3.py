"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.3
* 프로그램의 목적 및 기본 기능 :
* -Date Sorting with class date
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""


class Date:
    def __init__(self, y=1, m=1, d=1):
        self.setYear(y)
        self.setMonth(m)
        self.setDay(d)

    def __str__(self):
        s = "Date({:>4}-{:>02d}-{:>02d})".format(self.year, self.month, self.day)
        return s

    def setYear(self, yr):
        if yr > 0:
            self.year = yr

    def setMonth(self, mn):
        if mn > 0:
            self.month = mn

    def setDay(self, dy):
        if dy > 0:
            self.day = dy

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__eq__(other):
            return False
        elif (self.year, self.month, self.day) < (other.year, other.month, other.day):
            return True
        else:
            return False

    def __le__(self, other):
        if self.__eq__(other):
            return True
        elif self.__lt__(other):
            return True
        else:
            return False


def main():
    dates = [
        Date(2000, 9, 15),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1)
    ]
    print("dates before sorting : ")
    for d in dates:
        print(d)
    #
    dates.sort()
    print("\nstudents after sorting : ")
    for d in dates:
        print(d)


if __name__ == "__main__":
    main()
