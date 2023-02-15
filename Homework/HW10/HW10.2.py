"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW10.2
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
    A = np.array([[10, 10, 0, 0, 0], [1, -1, -1, 0, 0], [0, 0, 1, -1, -1], [0, 10, -5, -10, 0], [0, 0, 0, 10, -10]])
    B = np.array([100, 0, 0, 0, 0])
    X = np.linalg.solve(A, B)
    print("A = \n{}".format(A))
    print("B = {}".format(B))
    print("X = {}".format(X))
    print("np.matmul(A, X) = {}".format(np.matmul(A, X)))


if __name__ == "__main__":
    main()
