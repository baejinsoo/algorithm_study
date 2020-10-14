from collections import deque

N = int(input())
adv = list(map(int, input().split()))
num = 0

adv.sort(reverse=True)
q = deque(adv)
result = [[] for _ in range(N)]
j = 0
while q:
    index = q.popleft()
    result[j].append(index)
    for i in range(index-1):
        result[j].append(q.popleft())
    j += 1

for r in result:
    if r:
        num += 1

print(num)
