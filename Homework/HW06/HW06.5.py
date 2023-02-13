"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW06.5
* 프로그램의 목적 및 기본 기능 :
* -Matrix calculation with User defined module
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import sys
myPyPackage_dir = "C:/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyMatrix


def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 1]]
    B = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]
    C = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    print("A = ")
    MyMatrix.printMtrx(A)
    print("B = ")
    MyMatrix.printMtrx(B)
    print("C = ")
    MyMatrix.printMtrx(C)
    D = MyMatrix.mtrxAdd(A, B)
    print("A + B = ")
    MyMatrix.printMtrx(D)
    E = MyMatrix.mtrxSub(A, B)
    print("A - B = ")
    MyMatrix.printMtrx(E)
    F = MyMatrix.mtrxMul(A, C)
    print("A * C = ")
    MyMatrix.printMtrx(F)


if __name__ == "__main__":
    main()
