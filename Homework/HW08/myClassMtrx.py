"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW08.3 - myClassMtrx
* 프로그램의 목적 및 기본 기능 :
* -myClassMtrx module
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""
class Mtrx:
    def __init__(self, name, n_row, n_col, L_data):     # init class object
        self.Mtrx_Data = []
        index = 0
        self.setName(name)
        if n_row > 0:                                   # n_row valid check
            self.Row = n_row
        if n_col > 0:                                   # n_col valid check
            self.Col = n_col
        for i in range(0, self.Row):                    # 리스트를 Mtrx로 변환
            list_row = []
            for j in range(0, self.Col):
                list_row.append(L_data[index])
                index += 1
            self.Mtrx_Data.append(list_row)


    def setName(self, name):                            # setName
        self.Name = name

    def __str__(self):                                  # printout
        re_str = "{} =\n".format(self.Name)
        for i in range(0, self.Row):
            for p in range(0, self.Col):
                re_str += "{:>6}".format(str((self.Mtrx_Data[i][p])))       # Mtrx Data를 str형태로 변환
            re_str += "\n"
        return re_str

    def __add__(self, other):                           # operator overloading +
        re_Mtrx = []
        for i in range(0, self.Row):
            for p in range(0, self.Col):
                re_Mtrx.append(self.Mtrx_Data[i][p] + other.Mtrx_Data[i][p])    # add
        return Mtrx("M", self.Row, self.Col, re_Mtrx)

    def __sub__(self, other):                           # operator overloading ‐
        re_Mtrx = []
        for i in range(0, self.Row):
            for p in range(0, self.Col):
                re_Mtrx.append(self.Mtrx_Data[i][p] - other.Mtrx_Data[i][p])    # sub
        return Mtrx("M", self.Row, self.Col, re_Mtrx)

    def __mul__(self, other):                           # operator overloading *
        calc = 0
        re_Mtrx = []
        for i in range(0, self.Row):
            for p in range(0, other.Col):
                calc = 0
                for q in range(0, self.Col):
                    calc += self.Mtrx_Data[i][q] * other.Mtrx_Data[q][p]
                re_Mtrx.append(calc)                    # 곱셈 연산 결과 append
        return Mtrx("M", self.Row, other.Col, re_Mtrx)
