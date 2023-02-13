"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW07.5 - Class Mtrx
* 프로그램의 목적 및 기본 기능 :
* -Class Mtrx
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.10
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.10	v1.0	최초 작성
"""


class Mtrx:
    def __init__(self, name, n_row, n_col, lst_data):
        self.n_row = n_row
        self.n_col = n_col
        self.setName(name)
        lst_row = []
        self.rows = []
        index = 0
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                lst_row.append(lst_data[index])
                index = index + 1
            self.rows.append(lst_row)
            lst_row = []

    def __str__(self):
        s = self.name +"\n"
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                s += "{:3d}".format(self.rows[i][j])
            s += "\n"
        return s

    def __add__(self, other):  # operator overloading of '+'
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij = self.rows[i][j] + other.rows[i][j]
                lst_res.append(r_ij)
        return Mtrx("R", self.n_row, self.n_col, lst_res)

    def __sub__(self, other):  # operator overloading of '+'
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij = self.rows[i][j] - other.rows[i][j]
                lst_res.append(r_ij)
        return Mtrx("R", self.n_row, self.n_col, lst_res)

    def __mul__(self, other):  # operator overloading of '*'
        lst_res = []
        for i in range(0, self.n_row):
            for j in range(0, other.n_col):
                r_ij = 0
                for k in range(0, self.n_col):
                    r_ij = r_ij + self.rows[i][k] * other.rows[k][j]
                lst_res.append(r_ij)
        return Mtrx("R", self.n_row, other.n_col, lst_res)

    def setName(self, nm):
        self.name = nm
