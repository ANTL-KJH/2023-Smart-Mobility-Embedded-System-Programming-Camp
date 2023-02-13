"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.1
* 프로그램의 목적 및 기본 기능 :
* -Person data processing with class
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
from Class_Person import *

def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)

def main():
    persons = [
        Person("Kim", 990101, 21),
        Person("Lee", 980715, 22),
        Person("Park", 101225, 20),
        Person("Hong", 110315, 19),
        Person("Yoon", 971005, 23),
        Person("Wrong", 100000, 350)
    ]
    print("persons : ")
    printPersonList(persons)


if __name__ == "__main__":
    main()
