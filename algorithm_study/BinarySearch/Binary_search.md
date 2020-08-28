### 이진 탐색



##### 순차 탐색(시간복잡도 O(N))

- 데이터 정렬여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인

```python
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target
        	return i+1
```



##### 이진 탐색 (시간복잡도 O(logN))

- 배열 내부가 정렬되어 있어야만 사용 가능
- 중간점을 지정해서 찾으려는 값과 비교해 반은 버리고 탐색

```python
# 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)
```

```python
# 반복문
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None
```



##### 이진트리

