"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW06.5 - MyMatrix
* 프로그램의 목적 및 기본 기능 :
* -MyMatrix module
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.09
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.09	v1.0	최초 작성
"""


def printMtrx(L):
    for i in range(len(L)):
        for j in range(len(L[i])):
            print("{:>3}".format(L[i][j]), end="")
        print()


def mtrxAdd(mA, mB):
    mR = []
    for i in range(len(mA)):
        mT = []
        for p in range(len(mA[0])):
            mT.append(mA[i][p] + mB[i][p])
        mR.append(mT)
    return mR


def mtrxSub(mA, mB):
    mR = []
    for i in range(len(mA)):
        mT = []
        for p in range(len(mA[0])):
            mT.append(mA[i][p] - mB[i][p])
        mR.append(mT)
    return mR


def mtrxMul(mA, mB):
    mR = []
    for i in range(len(mA)):
        mT = []
        for j in range(len(mB[0])):
            result = 0
            for k in range(len(mA[0])):
                result += mA[i][k] * mB[k][j]
            mT.append(result)
        mR.append(mT)
    return mR