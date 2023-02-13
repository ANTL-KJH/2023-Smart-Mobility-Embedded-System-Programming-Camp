"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.2
* 프로그램의 목적 및 기본 기능 :
* -Student data processing with class inheritance
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
from Class_Person import *


class Student(Person):
    def __init__(self, name, reg_id, age, st_id, major, gpa):
        Person.__init__(self, name, reg_id, age)
        self.setMajor(major)
        self.setSTID(st_id)
        self.setGPA(gpa)

    def getMajor(self):
        return self.major

    def getSTID(self):
        return self.st_id

    def getGPA(self):
        return self.GPA

    def setMajor(self, major):
        # checking available major
        set_majors = {"EE", "ICE", "ME", "CE"}
        if major in set_majors:
            self.major = major
        else:
            print("*** Error in setting major (name:{}, age:{})".format(self.name, major))
            self.major = None

    def setSTID(self, st_id):
        # include checking correctness of ST_ID here
        self.st_id = st_id

    def setGPA(self, gpa):
        # include checking correct range of GPA
        self.GPA = gpa

    def __lt__(self, other):
        # if (self.st_id < other.st_id):
        # if (self.age < other.age):
        if (self.GPA > other.GPA):
            return True
        else:
            return False

    def __str__(self):
        return "Student({}, {}, {}, {}, {}, {})".format(self.getName(), self.getRegID(), self.getAge(), self.getSTID(),
                                                        self.getMajor(), self.getGPA())


def compareStudent(st1, st2, compare):
    if compare == "st_id":
        if st1.st_id < st2.st_id:
            return True
        else:
            return False


def sortStudent(L_st, compare):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i + 1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], compare):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]


def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])


def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)


def main():
    students = [
        Student("Kim", 990101, 21, 12345, "EE", 4.0),
        Student("Lee", 980715,22, 11234, "ME", 4.2),
        Student("Park", 101225,20, 10234, "ICE", 4.3),
        Student("Hong", 110315,19, 13123, "CE", 4.1),
        Student("Yoon", 100000,23, 11321, "ICE", 4.2)
    ]
    print("students before sorting : ")
    printStudents(students)

    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)

    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)

    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)


if __name__ == "__main__":
    main()
