"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW08.2
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


def calculate_score(data_list):
    i = 0
    sumKor = 0
    sumEng = 0
    sumMath = 0
    sumSci = 0
    num_class = 4
    for name, kor, eng, math, sci in data_list:
        sumScore = kor + eng + math + sci
        data_list[i].append(sumScore)
        data_list[i].append(sumScore / num_class)
        sumKor += kor
        sumEng += eng
        sumMath += math
        sumSci += sci
        i += 1
    return (sumKor, sumEng, sumMath, sumSci)


def fwrite_data(file_name, data_list):
    fout = open(file_name, 'w')
    fout.write("{:^5s}{:>5}{:>5s}{:>5s}{:>5s}{:>5s}{:^7s}\n".format("name", "kor", "eng", "math", "sci", "sum", "avg"))
    fout.write("-" * 37 + "\n")
    for data in data_list:
        s = "{:<5s}".format(data[0])
        s += "{:>5}".format(data[1])
        s += "{:>5}".format(data[2])
        s += "{:>5}".format(data[3])
        s += "{:>5}".format(data[4])
        s += "{:5d}".format(data[5])
        s += "{:7.2f}".format(data[6])
        s += "\n"
        fout.write(s)
    fout.close()


def fread_data(file_name):
    data_list = []
    fin = open(file_name, 'r')
    for line in fin:
        name, kor, eng, math, sci = line.split()
        tmp = [name, int(kor), int(eng), int(math), int(sci)]
        data_list.append(tmp)
    fin.close()
    return data_list


def main():
    students = fread_data("student_records.txt")
    for st in students:
        print(st)
    (sumKor, sumEng, sumMath, sumSci) = calculate_score(students)

    print("\nAfter calculate_student_score(students)")
    print("{:^5s}{:>5}{:>5s}{:>5s}{:>5s}{:>5s}{:^7s}".format("name", "kor", "eng", "math", "sci", "sum", "avg"))
    for data in students:
        s = "{:<5s}".format(data[0])
        s += "{:>5}".format(data[1])
        s += "{:>5}".format(data[2])
        s += "{:>5}".format(data[3])
        s += "{:>5}".format(data[4])
        s += "{:5d}".format(data[5])
        s += "{:7.2f}".format(data[6])
        print(s)
    fwrite_data("output.txt", students)

    print("\nAverage score of each class :")
    print("Kor_avg = {}".format(sumKor / len(students)))
    print("Eng_avg = {}".format(sumEng / len(students)))
    print("Math_avg = {}".format(sumMath / len(students)))
    print("Sci_avg = {}".format(sumSci / len(students)))


if __name__ == "__main__":
    main()
