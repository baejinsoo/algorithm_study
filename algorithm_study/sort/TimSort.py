import random

# 시간 복잡도: 최상(n), 평균(n^2), 최악(n^2)


def insertSort(array, left, right):
    for i in range(left + 1, right + 1):
        temp = array[i]
        j = i - 1
        while j >= left and array[j] > temp:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array


def fastmerge(array1, array2):
    merged_array = []
    while array1 or array2:
        if not array1:
            merged_array.append(array2.pop())
        elif (not array2) or array1[-1] > array2[-1]:
            merged_array.append(array1.pop())
        else:
            merged_array.append(array2.pop())
    merged_array.reverse()
    return merged_array


MIN_MERGE = 64


def timSort(arr):
    def calcMinRun(n):
        """Returns the minimum length of a run from 23 - 64 so that
        the len(array)/minrun is less than or equal to a power of 2.

        e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33, ..., 127=>64, 128=>32, ...
        """
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1
            n >>= 1
        return n + r

    n = len(arr)
    minRun = calcMinRun(n)

    # min run 만큼 건너뛰면서 삽입 정렬 실행
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        arr = insertSort(arr, start, end)
    currentSize = minRun

    # minRun이 배열 길이보다 작을 때까지만 minRun * 2 를 한다.
    while currentSize < n:
        for start in range(0, n, currentSize * 2):
            mid = min(n - 1, start + currentSize - 1)
            right = min(start + 2*currentSize - 1, n - 1)
            merged = fastmerge(array1=arr[start:mid + 1],
                               array2=arr[mid + 1:right + 1])
            arr[start:start + len(merged)] = merged

        currentSize *= 2

    return arr


arr = []
for i in range(150):
    num = random.randrange(-100, 100)
    arr.append(num)

print(timSort(arr))
