"""
* 프로젝트명 : Smart Mobility Embedded System Programming Camp HW05.2
* 프로그램의 목적 및 기본 기능 :
* -Compare selection, merge, quick sorting Algorithms
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import random, time


# merge Sorting
def _merge(L_left, L_right):
    L_result = []
    i, j = 0, 0
    while i < len(L_left) and j < len(L_right):
        if L_left[i] < L_right[j]:
            L_result.append(L_left[i])
            i += 1
        else:
            L_result.append(L_right[j])
            j += 1
    while (i < len(L_left)):
        L_result.append(L_left[i])
        i += 1
    while (j < len(L_right)):
        L_result.append(L_right[j])
        j += 1
    return L_result


def _mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = _mergeSort(L[:middle])
        L_right = _mergeSort(L[middle:])
        L_result = _merge(L_left, L_right)
        return L_result


# merge_sort in increasing order
def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        L_result = _mergeSort(L)
    for i in range(len(L)):
        L[i] = L_result[i]


# Quick Sorting
def _partition(arr, left, right, pi):
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    npi = i = left  # npi : new pivot index
    while (i <= right - 1):
        if (arr[i] <= pv):
            arr[npi], arr[i] = arr[i], arr[npi]
            npi += 1
        i += 1
    arr[npi], arr[right] = arr[right], arr[npi]
    return npi


def _quickSortLoop(arr, left, right):
    # print("quickSort", left, right)
    if (left >= right):
        return
    pi = (left + right) // 2  # pivot index
    new_pi = _partition(arr, left, right, pi)
    # print("after partition : ", left, right, new_pi)
    if (left < new_pi - 1):
        _quickSortLoop(arr, left, new_pi - 1)
    if (new_pi + 1 < right):
        _quickSortLoop(arr, new_pi + 1, right)


def quickSort(arr):
    left, right = 0, len(arr) - 1  # indices of sorting region
    _quickSortLoop(arr, left, right)


# printout Samples
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


# Selection Sorting
def selectionSort(L):
    size = len(L)
    for i in range(0, size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if (L[min_idx] > L[j]):
                min_idx = j
        if (min_idx != i):
            L[min_idx], L[i] = L[i], L[min_idx]


# Random List Generator
def genRandList(L, size):
    for i in range(size):
        L.append(i)
    random.shuffle(L)


def main():
    while True:
        size = int(input("\nsize of list (0 to terminate) = "))  # input size
        if size == 0:
            break
        L = []
        genRandList(L, size)  # genRandList

        # Selection Sorting
        # print("List (size : {}) before selection sorting : ".format(size))
        # printListSample(L, 10, 2)  # printout samples
        # t1 = time.time()  # time check
        # selectionSort(L)  # merge sorting
        # t2 = time.time()  # time check
        # print("\nList (size : {}) after selection sorting : ".format(size))
        # printListSample(L, 10, 2)  # printout samples
        # print("Selection sorting for list of {} integers took {} sec".format(size, t2 - t1))
        # random.shuffle(L)

        # Merge Sorting
        print("List (size : {}) before merge sorting : ".format(size))
        printListSample(L, 10, 2)  # printout samples
        t1 = time.time()  # time check
        mergeSort(L)  # merge sorting
        t2 = time.time()  # time check
        print("\nList (size : {}) after merge sorting : ".format(size))
        printListSample(L, 10, 2)  # printout samples
        print("Merge sorting for list of {} integers took {} sec".format(size, t2 - t1))
        random.shuffle(L)

        # Quick Sorting
        print("\nList (size : {}) before quick sorting : ".format(size))
        printListSample(L, 10, 2)  # printout samples
        t1 = time.time()  # time check
        quickSort(L)  # merge sort
        t2 = time.time()  # time check
        print("\nList (size : {}) after selection sorting : ".format(size))
        printListSample(L, 10, 2)  # printout samples
        print("Quick sorting sorting for list of {} integers took {} sec".format(size, t2 - t1))


if __name__ == "__main__":
    main()
