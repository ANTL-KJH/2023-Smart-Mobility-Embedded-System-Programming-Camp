"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW06.2
* 프로그램의 목적 및 기본 기능 :
* -genRandList and Sorting with MyList and sys module
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
from MyPyPackage.myModules import MyList, MySortings


def main():
    L = []
    n = 100
    MyList.genRandList(L, n)
    print("Before Sorting :")
    MyList.printListSample(L, 10, 3)
    MySortings.selectionSort(L)
    print("\nAfter Sorting :")
    MyList.printListSample(L, 10, 3)


if __name__ == "__main__":
    main()
