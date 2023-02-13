"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW08.1
* 프로그램의 목적 및 기본 기능 :
* -genRandList with MyList and sys module
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""


def main():
    country = []
    fin = open("demography.txt", 'r')
    for line in fin:
        name, capital, people, area = line.split()
        country.append((name, capital, people, area))
    print("List of countries:")
    for i in range(len(country)):
        print("Country[{:2}] : {}".format(i, country[i]))

    country.sort(key=lambda x: int(x[2]), reverse=1)

    print("\nList of countries sorted by demography(number of people) :")
    for i in range(len(country)):
        print("Country[{:2}] : {}".format(i, country[i]))
    fin.close()


if __name__ == "__main__":
    main()
