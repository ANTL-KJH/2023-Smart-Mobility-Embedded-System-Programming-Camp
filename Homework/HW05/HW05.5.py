"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW05.5
* 프로그램의 목적 및 기본 기능 :
* -Matrix calculation and printing with function
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""


def printMtrx(name, m):
    print("{} = ".format(name))
    for i in range(len(m)):
        for p in range(len(m[i])):
            print("{:3}".format(m[i][p]), end="")
        print()
    return


def addMtrx(mA, mB):
    mR = []
    for i in range(len(mA)):
        mT = []
        for p in range(len(mA[0])):
            mT.append(mA[i][p] + mB[i][p])
        mR.append(mT)
    return mR


def subMtrx(mA, mB):
    mR = []
    for i in range(len(mA)):
        mT = []
        for p in range(len(mA[0])):
            mT.append(mA[i][p] - mB[i][p])
        mR.append(mT)
    return mR


def mulMtrx(M1, M2):
    mR = []
    for i in range(len(M1)):
        mT = []
        for j in range(len(M2[0])):
            result = 0
            for k in range(len(M1[0])):
                result += M1[i][k] * M2[k][j]
            mT.append(result)
        mR.append(mT)
    return mR


def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
    B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
    C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    printMtrx("A", A)
    printMtrx("B", B)
    printMtrx("C", C)
    D = addMtrx(A, B)
    printMtrx("A + B", D)
    E = subMtrx(A, B)
    printMtrx("A - B", E)
    F = mulMtrx(A, C)
    printMtrx("A * C", F)


if __name__ == "__main__":
    main()
