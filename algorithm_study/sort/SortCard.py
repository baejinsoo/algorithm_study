# BOJ 1715 카드 정렬하기
# 우선순위 큐 => 원소를 넣었다 빼는 것만으로 정렬된 결과를 얻을 수 있음
import heapq


n = int(input())
card = []
heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)
result = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum_card = a + b
    result += sum_card
    heapq.heappush(heap, sum_card)

print(result)

