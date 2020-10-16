from collections import deque


N, M, K, X = map(int, input().split())
node = [[] for _ in range(N + 1)]
distance = [-1] * (N + 1)
distance[X] = 0
q = deque([X])

for _ in range(M):
    a, b = map(int, input().split())
    node[a].append(b)

while q:
    now = q.popleft()
    for i in node[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)

check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)
