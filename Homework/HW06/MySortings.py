"""
* 프로젝트명 : MySortings
* 프로그램의 목적 및 기본 기능 :
* -MySortings
* 프로그램 작성자 : JH KIM
* 최초 프로그램 작성일 : 2023.02.08
* ======================================================================================
* 프로그램 수정 / 보완 이력
* ======================================================================================
* 프로그램 수정자		일자			버전		수정내용
* JH KIM			2023.02.08	v1.0	최초 작성
"""
import time


def measureTime(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("WorkingTime[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn


# SelectionSorting
#@measureTime
def selectionSort(L):
    size = len(L)
    for i in range(0, size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if (L[min_idx] > L[j]):
                min_idx = j
        if (min_idx != i):
            L[min_idx], L[i] = L[i], L[min_idx]


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
@measureTime
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

@measureTime
def quickSort(arr):
    left, right = 0, len(arr) - 1  # indices of sorting region
    _quickSortLoop(arr, left, right)