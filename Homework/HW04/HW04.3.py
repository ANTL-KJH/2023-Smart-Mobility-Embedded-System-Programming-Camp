"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW04.3
* 프로그램의 목적 및 기본 기능 :
* -사용자로부터 10개의 날짜를 입력받고 정렬하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def main():
    Date_List = []  # Date List
    for i in range(0, 10):
        (yr, mn, dy) = tuple(map(int, (input("input year, month, day : ")).split(sep=" ")))
        Date_List.append((yr, mn, dy))  # append tuple
        print("Date_List = ", Date_List)

    print("\nAfter input of 10 dates")
    print("Date_List = ", Date_List, end="\n\n")    # printout List

    print("After sorting, Date_List")
    Date_List.sort()                    # sorting
    print("Date_List = ", Date_List)


if __name__ == "__main__":
    main()
