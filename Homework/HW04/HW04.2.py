"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW04.2
* 프로그램의 목적 및 기본 기능 :
* -두 2차원 배열의 곱셈연산을 하고 결과를 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def printMtrx(m):
    for i in range(len(m)):
        for p in range(len(m[i])):
            print("{:2}".format(m[i][p]), end="")
        print()


def mulMtrx(M1, M2):    # Matrix Multiply
    Mtrx = []
    col = len(M2[1])    # col size
    row = len(M1)       # row size

    for i in range(0, row):
        temp_row = []
        for j in range(0, col):
            result = 0
            for k in range(0, len(M1[1])):
                result += M1[i][k] * M2[k][j]
            temp_row.append(result)
        Mtrx.append(temp_row)
    return Mtrx


def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    print("A =")
    printMtrx(A)
    print("B =")
    printMtrx(B)
    C = mulMtrx(A, B)
    print("C = A * B =")
    printMtrx(C)


if __name__ == "__main__":
    main()
