"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW04.4
* 프로그램의 목적 및 기본 기능 :
* -Student Data를 정렬하여 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def main():
    # Student Data
    Student_name = ['Kim, S.C.', 'Choi, Y.B.', 'Hong, C.H', 'Yoon, J.H', 'Lee, S.H', 'Kim, H.Y', 'Lee, J.K',
                    'Park, S.Y', 'Jang, S.H', 'Yeo, C.S']
    Student_id = [12001234, 119003234, 21001547, 17002571, 20003257, 19001234, 18003234, 21001643, 19002567, 20005243]
    Student_major = ['CE', 'EE', 'ICE', 'ME', 'ICE', 'CE', 'EE', 'ICE', 'ME', 'CE']
    Student_GPA = [4.10, 3.78, 4.13, 3.55, 4.45, 4.17, 3.78, 4.13, 3.35, 4.45]
    students_data = list(zip(Student_name, Student_id, Student_major, Student_GPA))

    # Printout Student Data
    for i in range(0, 10):
        (st_n, st_i, st_m, st_g) = students_data[i]
        print("students[{0:2}] : name({1:8}), st_id({2:8}), major({3:3}, GPA({4:5.2f}))".format(i, st_n, st_i, st_m,
                                                                                                st_g))

    students_data.sort()  # sorting
    print("\nAfter sorting in increasing order : ")
    for i in range(0, 10):
        (st_n, st_i, st_m, st_g) = students_data[i]
        print("students[{0:2}] : name({1:8}), st_id({2:8}), major({3:3}, GPA({4:5.2f}))".format(i, st_n, st_i, st_m,
                                                                                                st_g))

    # GPA를 기준으로 내림차순 sorting
    sorted_students = sorted(students_data, key=lambda std: std[3], reverse=True)

    print("\nAfter sorting according to GPA in decreasing order : ")
    for i in range(0, 10):
        (st_n, st_i, st_m, st_g) = sorted_students[i]
        print("students[{0:2}] : name({1:8}), st_id({2:8}), major({3:3}, GPA({4:5.2f}))".format(i, st_n, st_i, st_m,
                                                                                                st_g))


if __name__ == "__main__":
    main()
