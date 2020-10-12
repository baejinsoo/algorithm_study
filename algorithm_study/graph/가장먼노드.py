# 프로그래머스 가장 먼 노드

from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v,count = value
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])


def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    for e in edge:
        x, y = e
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
x = solution(n, edge)
print(x)