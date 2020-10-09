# 백준 1504 특정한 최단경로
INF = int(1e9)
N, E = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for a in range(N+1):
    for b in range(N+1):
        if a == b:
            graph[a][b] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

for k in range(N+1):
    for a in range(N + 1):
        for b in range(N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance = graph[1][v1] + graph[v1][v2] + graph[v2][N]
if distance >= INF:
    print("-1")
else:
    print(distance)