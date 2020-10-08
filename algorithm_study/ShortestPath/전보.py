import heapq
INF = int(1e9)

n,m,c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            time = dist + i[1]
            if time < distance[i[0]]:
                distance[i[0]] = time
                heapq.heappush(q,(time, i[0]))


dijkstra(c)
check = 0
max = 0
for i in range(1, n+1):
    if distance[i] == INF:
        continue
    else:
        print(i, distance[i])
        check += 1
        if distance[i] > max:
            max = distance[i]
print(check-1, max)
