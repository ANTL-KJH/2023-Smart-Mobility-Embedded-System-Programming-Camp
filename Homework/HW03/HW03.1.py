"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW03.1
* 프로그램의 목적 및 기본 기능 :
* -사용자로부터 생일을 입력받고 요일, 탄생석을 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.06
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.06	v1.0	최초 작성
"""


def main():
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    birthstone = ["", "Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl", "Ruby", "Peridot", "Sapphire",
                  "Opal", "Topaz", "Turquoise"]

    while True:
        yr, mn, dy = map(int, input("Input your birth date (year month day) : ").split())
        if yr == 0 or mn == 0 or dy == 0:
            break
        print("Your birth date = year({}), month({}), day({}) :".format(yr, mn, dy))

        elapsed_day = dy
        if yr % 4 == 0 and yr % 100 != 0 or yr % 400 == 0:
            month[2] = 29
        else:
            month[2] = 28

        for i in range(1, mn):
            elapsed_day += month[i]

        for i in range(1, yr):
            if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
                elapsed_day += 366
            else:
                elapsed_day += 365
        print("elapsed {} days from JAN01AD01, week day = {}, birth_stone = {}".format(elapsed_day,
                                                                                       week_day[elapsed_day % 7],
                                                                                       birthstone[mn]))


if __name__ == "__main__":
    main()
