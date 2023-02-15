"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.5
* 프로그램의 목적 및 기본 기능 :
* -Matrix calculation with class and User defined module
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.10
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.10	v1.0	최초 작성
"""
from Class_Mtrx import *


def main():
    L_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    L_2 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
    L_3 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    m1 = Mtrx("M1", 4, 5, L_1)
    print(m1)
    m2 = Mtrx("M2", 4, 5, L_2)
    print(m2)
    m3 = Mtrx("M3", 5, 4, L_3)
    print(m3)

    m4 = m1 + m2        # matrix add
    m4.setName("M4 = M1 + M2")
    print(m4)

    m5 = m1 - m2        # matrix sub
    m5.setName("M5 = M1 - M2")
    print(m5)

    m6 = m1 * m3        # matrix mul
    m6.setName("M6 = M1 * M3")
    print(m6)


if __name__ == "__main__":
    main()
