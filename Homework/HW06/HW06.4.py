"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW06.4
* 프로그램의 목적 및 기본 기능 :
* -Speed compare merge sorting with selection sorting
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import random, time, sys
sys.path.append("C:/")
from MyPyPackage.myModules import MyList, MySortings


def main():
    while True:
        size = int(input("\nsize of list (0 to terminate) = "))
        if size == 0:
            break
        L = []
        MyList.genRandList(L, size)
        print("List (size : {}) before merge sorting : ".format(size))
        MyList.printListSample(L, 10, 2)
        t1 = time.time()
        MySortings.mergeSort(L)
        t2 = time.time()
        print("\nList (size : {}) after merge sorting : ".format(size))
        MyList.printListSample(L, 10, 2)
        print("Merge sorting for list of {} integers took {} sec".format(size, t2 - t1))
        MyList.shuffleList(L)
        print("\nList (size : {}) before selection sorting : ".format(size))
        MyList.printListSample(L, 10, 2)
        t1 = time.time()
        MySortings.selectionSort(L)
        t2 = time.time()
        print("\nList (size : {}) after selection sorting : ".format(size))
        MyList.printListSample(L, 10, 2)
        print("Selection sorting for list of {} integers took {} sec".format(size, t2 - t1))


if __name__ == "__main__":
    main()
