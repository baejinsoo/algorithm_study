# BOJ 1715 카드 정렬하기
# 우선순위 큐 => 원소를 넣었다 빼는 것만으로 정렬된 결과를 얻을 수 있음
from collections import deque

data = 'HELLO'
q = deque(data)
result = q.pop() + q.pop()
print(result)

