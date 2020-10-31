import random


## 함수 선언부
def insertionSort(before) :
    def findMinIdx(arr):
        retIdx = 0
        for i in range(len(arr)):
            if arr[retIdx] > arr[i]:
                retIdx = i
        return retIdx
    newarr = []
    for i in range(len(before)):
        minInx = findMinIdx(before)
        newarr.append(before[minInx])
        del(before[minInx])
    return newarr

## 전역 변수부
before = [ random.randint(10, 99) for _ in range(20) ]
after = []


## 메인 코드부
print(before)
after = insertionSort(before)
# for i in range(len(before)):
#     minIdx = findMinIdx(before)
#     after.append(before[minIdx])
#     del(before[minIdx])
print(after)
