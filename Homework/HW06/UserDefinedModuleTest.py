"""
* 프로젝트명 : Smart Mobility Embeded System Programming Camp HW06.1
* 프로그램의 목적 및 기본 기능 :
* -students Data를 분석하여 출력하는 프로그램
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import MyList
import MySortings

def main():
    L = []
    MyList.genRandList(L, 10000)

    print("generated random float list (before sorting) :")
    MyList.printListSample(L, 10, 3)
    MySortings.selectionSort(L)
    print("after SelectionSorting :")
    MyList.printListSample(L, 10, 3)

    print("generated random float list (before sorting) :")
    MyList.printListSample(L, 10, 3)
    MySortings.mergeSort(L)
    print("after MergeSorting :")
    MyList.printListSample(L, 10, 3)

    print("generated random float list (before sorting) :")
    MyList.printListSample(L, 10, 3)
    MySortings.quickSort(L)
    print("after QuickSorting :")
    MyList.printListSample(L, 10, 3)


if __name__ == "__main__":
    main()
