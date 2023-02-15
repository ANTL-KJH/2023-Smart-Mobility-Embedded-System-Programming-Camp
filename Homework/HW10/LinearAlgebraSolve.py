"""
* 프로젝트명 : 2023 SMESPC Linear Algebra Solve
* 프로그램의 목적 및 기본 기능 :
* -electric circuit analysis with numpy package
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.10
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.10	v1.0	최초 작성
"""
import numpy as np


def main():
    A = np.array([[1, 1, 1], [2, 3, 1], [1, -1, -1]])
    B = np.array([4, 9, -2])
    X = np.linalg.solve(A, B)
    B1 = np.matmul(A, X)
    invA = np.linalg.inv(A)
    X1 = np.matmul(invA, B)

    print("A =\n", A)
    print("B = ", B)
    print("X = np.linalg.solve(A)")
    print("X = ", X)
    print("B1  np.matmul(A, X) = ", B1)

    print("invA = ",invA)
    print("X1 = ", X1)

if __name__ == "__main__":
    main()
