"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW06.3
* 프로그램의 목적 및 기본 기능 :
* -Speed Compare array with list
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import random, time, sys
from array import *

sys.path.append("C:/")
from MyPyPackage.myModules import MyList, MySortings


def main():
    AR = array('i')
    L = []
    size = 10000
    MyList.genRandList(L, size)
    for x in L:
        AR.append(x)
    print("Array (size : {}) before sorting : ".format(size))
    MyList.printListSample(AR, 10, 2)
    t1 = time.time()
    MySortings.selectionSort(AR)
    t2 = time.time()
    print("Array (size : {}) after sorting : ".format(size))
    MyList.printListSample(AR, 10, 2)
    print("Selection sorting for array of {} integers took {} sec".format(size, t2 - t1))
    print("\nList (size : {}) before sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    t1 = time.time()
    MySortings.selectionSort(L)
    t2 = time.time()
    print("\nList (size : {}) after sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    print("Selection sorting for list of {} integers took {} sec".format(size, t2 - t1))


if __name__ == "__main__":
    main()
