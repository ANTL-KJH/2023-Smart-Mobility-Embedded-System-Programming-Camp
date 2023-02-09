"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW05.1
* 프로그램의 목적 및 기본 기능 :
* -students Data를 분석하여 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""


def main():
    students = (('Kim', 'EE', 12345, (2000, 12, 25), 4.0),
                ('Lee', 'ME', 11234, (2019, 9, 1), 4.2),
                ('Park', 'ICE', 10234, (2019, 3, 1), 4.3),
                ('Hong', 'CE', 13123, (2021, 1, 1), 4.1),
                ('Yoon', 'ICE', 11321, (2001, 8, 15), 4.2),
                ('A', 'ICE', 12321, (2000, 7, 31), 4.2)
                )
    L = []
    print("students = ")
    for i in range(len(students)):
        print(students[i])
        L.append(students[i][4])

    L.sort()
    print("statistics_student_GPA ::")
    print(" - L_GPAs = {}".format(L))
    print(" - num_students = {}".format(len(students)))
    print(" - Statistics of GPAs : Max ({}), Min ({}), Avg ({})".format(max(L), min(L), sum(L) / len(L)))


if __name__ == "__main__":
    main()
