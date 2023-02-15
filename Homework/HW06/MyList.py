"""
* 프로젝트명 : MyList
* 프로그램의 목적 및 기본 기능 :
* -MyList
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import random

def printListSample(L, per_line=10, sample_lines=2):
    count = 0
    size = len(L)
    for i in range(0, sample_lines):
        s = ""
        for j in range(0, per_line):
            if count > size:
                break
            s += "{0:>7} ".format(L[count])
            count += 1
        print(s)
        if count >= size:
            break
    if count < size:
        print('. . . . . .')
        if count < (size - per_line * sample_lines):
            count = size - per_line * sample_lines
        for i in range(0, sample_lines):
            s = ""
            for j in range(0, per_line):
                if count >= size:
                    break
                s += "{0:>7} ".format(L[count])
                count += 1
            print(s)
            if count >= size:
                break

def genRandList(L, size):
    for i in range(size):
        L.append(i)
    random.shuffle(L)

def shuffleList(L):
    random.shuffle(L)