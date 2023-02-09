"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW04.5
* 프로그램의 목적 및 기본 기능 :
* -국가와 수도를 dict 형태로 저장하고 국가명으로 수도를 찾는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def main():
    nation_capital = []  # 튜플을 담을 리스트
    for i in range(0, 10):
        # input Country
        input_str = input("Input nation and its capital (. to quit) : ")
        if input_str == ".":  # input_str이 .이면 종료
            exit(0)
        (country, capital) = tuple(map(str, input_str.split(" ")))
        nation_capital.append((country, capital))

    dict_nation_capital = dict(nation_capital)  # dictionary list 생성

    print("dict_nation_capital :", dict_nation_capital)

    while True:
        key = input("Input nation to find its capital (. to quit) : ")  # 입력받은 country를 key로 value 출력
        if key == ".":
            break
        print("The capital of", key, "is", dict_nation_capital[key])


if __name__ == "__main__":
    main()
