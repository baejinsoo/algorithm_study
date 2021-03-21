from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n):
    x = list(map(int, input().split()))
    j = 1
    while x[j] != -1:
        graph[x[0]].append((x[j], x[j+1]))
        j += 2


def bfs(start):
    visit = [0] * (n+1)
    visit[start] = 1
    dist[start] = 0
    q = deque()
    for i in graph[start]:
        a, b = i
        dist[a] = b
        visit[a] = 1
        q.append(a)
    while q:
        now = q.popleft()
        for i in graph[now]:
            a, b = i
            if visit[a] == 1:
                continue
            visit[a] = 1
            dist[a] = b + dist[now]
            q.append(a)
    res = 0
    answer = 0
    for i in range(1, n+1):
        if res < dist[i]:
            res = dist[i]
            answer = i
    return answer


dist = [INF] * (n+1)
first = bfs(1)
tree = bfs(first)
print(dist[tree])

"""
INF = int(1e9)

n = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(n):
    x = list(map(int, input().split()))
    j = 1
    while x[j] != -1:
        graph[x[0]][x[j]] = x[j+1]
        j += 2

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, n+1):
    for j in range(1, n+1//2):
        answer = max(answer, graph[i][j])

print(answer)
"""
