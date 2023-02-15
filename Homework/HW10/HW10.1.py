"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW10.1
* 프로그램의 목적 및 기본 기능 :
* -normal distribution analysis with numpy package
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.10
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.10	v1.0	최초 작성
"""
import numpy as np


def printArraySample(arr, per_line=10, sample_lines=3):
    for i in range(sample_lines * per_line):
        print("{:8.2f}".format(arr[i]), end="")
        if i % 10 == 9:
            print()
    print("    . . . . .")
    for i in range(sample_lines * per_line):
        print("{:8.2f}".format(arr[len(arr) - (per_line * sample_lines) + i]), end="")
        if i % 10 == 9:
            print()


def main():
    while True:
        mu, sigma = map(float, input("mu and sigma(in float): ").split())
        size = int(input("size of array : "))
        if size == 0:
            break
        G = np.random.normal(mu, sigma, size)
        printArraySample(G, 10, 3)
        print("mean of G = {}".format(G.mean()))
        print("var of G = {}".format(G.var()))
        print("std of G = {}".format(G.std()))
        print()


if __name__ == "__main__":
    main()
