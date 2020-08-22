from collections import deque

# 도시개수, 도로개수, 거리정보, 출발 도시번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)
# 출발지점의 거리는 0
distance[x] = 0

#bfs
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동가능한 도시 체크
    for next_node in graph[now]:
        # 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1,len(distance)):
    if distance[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
