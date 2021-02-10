import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

res = 0
while len(q) >= 2:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    res += (first + second)
    heapq.heappush(q, (first + second))
print(res)
