"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW03.4
* 프로그램의 목적 및 기본 기능 :
* -selection Sorting Algorithms을 이용하여 주어진 리스트를 정렬하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.07
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.07	v1.0	최초 작성
"""


def main():
    L = [5, 3, 8, 1, 2, 7, 0, 4, 6, 9]
    size = len(L)
    print("L (initial) = {}".format(L))
    for i in range(size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if L[min_idx] > L[j]:
                min_idx = j
        if min_idx != i:
            L[min_idx], L[i] = L[i], L[min_idx]
        print("round{:2} - L : {}".format(i, L))


if __name__ == "__main__":
    main()
