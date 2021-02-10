import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bosucks = []
for _ in range(n):
    weight, cost = map(int, input().split())
    bosucks.append((weight, cost))

bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()
bosucks.sort()

result = 0
check = 0
q = []
for bag in bags:
    while check < n and bag >= bosucks[check][0]:
        heapq.heappush(q, -bosucks[check][1])
        check += 1
    if len(q) > 0:
        result += abs(heapq.heappop(q))

print(result)

# 이전의 가방보다 현재의 가방이 더 크기 때문에 이전 가방에 들어갈 수 있는 보석은
# 무조건 현재 가방에서도 가능하다. 따라서 우선순위 큐의 heapq를 사용하면 된다.