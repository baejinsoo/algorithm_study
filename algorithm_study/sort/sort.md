### 정렬

##### 선택정렬 (시간복잡도 O(N**2))

```python
array = [7,5,9,0,3,1,6,2,4]

for i in range(len(array):
    min_index = i
    for j in range(i+1,len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i] , array[min_index] = array[min_index], array[i]
```



##### 삽입정렬

- 거의 정렬되어 있는 상태인 경우(최선의 경우 시간복잡도 O(N))

```python
array = [7,5,9,0,3,1,6,2,4]

for i in range(1,len(array)):
    for j in range(i,0,-1): # 한 칸씩 왼쪽으로 이동하면서 반복
        if array[j] < array[j-1]: 
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
```



##### 퀵 정렬 (시간복잡도 O(NlogN))

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방식
- 피벗 사용(피벗 = 큰 숫자와 작은 숫자를 교환할 때 교환하기 위한 ''기준'')
  - 호어분할 방식 - 리스트에서 첫 번째 데이터를 피벗으로 설정
  - 왼쪽에서부터 피벗보다 큰 숫자선택, 오른쪽에서부터 피벗보다 작은 숫자선택하여 교환
  - 분할이 완료되면 왼쪽은 피벗보다 작은 숫자들, 오른쪽은 피벗보다 큰 숫자들로 정렬
  - 왼쪽과 오른쪽 각각 피벗설정하여 진행

```python
# 직관적인 퀵정렬 소스코드
array = [7,5,9,0,3,1,6,2,4]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 right데이터와 피벗을 교체
            array[pivot], array[right] = array[right], array[pivot]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
    
quick_sort(array,0,len(array)-1)
```

```python
# python의 장점을 살린 퀵 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗설정
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분
    
    # 분할 이후 각각 정렬 수행 후 전체리스트 반환
    return quick_sort(left_side) + [pivot] +quick_sort(right_side)
```

##### 계수 정렬 (시간복잡도 O(N+K)) (K: 데이터중 최대값)

- 특정한 조건이 부합할경우만 사용가능, 매우빠른 정렬 알고리즘

  - 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때

  - 모든 범위를 담을 수 있는 크기의 리스트를 선언해야함

- 데이터의 값과 동일한 인덱스에 넣음, 동일한 값이면 인덱스의 데이터를 증가시킴

```python
# 모든 원소 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,6,4,1,5,3,2,0]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    # 각 데이터에 해당하는 인덱스 값 증가
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```

