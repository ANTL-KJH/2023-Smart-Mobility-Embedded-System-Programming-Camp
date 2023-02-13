"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp Studnet Data Handling
* 프로그램의 목적 및 기본 기능 :
* -Studnet Data Handling
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""


def calculate_score(data_list):
    i = 0
    num_class = 3
    for name, kor, eng, math in data_list:
        sumScore = kor + eng + math
        data_list[i].append(sumScore)
        data_list[i].append(sumScore / num_class)
        i += 1


def fwrite_data(file_name, data_list):
    fout = open(file_name, 'w')
    fout.write("{:^5s}{:>5}{:>5s}{:>5s}{:>5s}{:^7s}\n".format("name", "kor", "eng", "math", "sum", "avg"))
    fout.write("-" * 32 + "\n")
    for data in data_list:
        s = "{:<5s}".format(data[0])
        s += "{:>5}".format(data[1])
        s += "{:>5}".format(data[2])
        s += "{:>5}".format(data[3])
        s += "{:5d}".format(data[4])
        s += "{:7.2f}".format(data[5])
        s += "\n"
        fout.write(s)
    fout.close()


def fread_data(file_name):
    data_list = []
    fin = open(file_name, 'r')
    for line in fin:
        name, kor, eng, math = line.split()
        tmp = [name, int(kor), int(eng), int(math)]
        data_list.append(tmp)
    fin.close()
    return data_list


def main():
    students = fread_data("data_student_records.txt")
    for st in students:
        print(st)
    calculate_score(students)
    print("\nAfter calculate_student_score(students)")
    print("{:^5s}{:>5}{:>5s}{:>5s}{:>5s}{:^7s}".format("name", "kor", "eng", "math", "sum", "avg"))
    for data in students:
        s = "{:<5s}".format(data[0])
        s += "{:>5}".format(data[1])
        s += "{:>5}".format(data[2])
        s += "{:>5}".format(data[3])
        s += "{:5d}".format(data[4])
        s += "{:7.2f}".format(data[5])
        print(s)
    fwrite_data("result_student.txt", students)


if __name__ == "__main__":
    main()
