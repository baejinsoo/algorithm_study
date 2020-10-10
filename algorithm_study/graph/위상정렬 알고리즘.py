# 위상정렬 알고리즘
# DAG(Direct Acyclic Graph: 순환하지 않는 방향 그래프)에 대해서만 수행가능
# 여러가지 답이 존재할 수 있음
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단 가능
# 사이클에 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못함
# 스택을 활용한 DFS를 이용해 위상 정렬 수행도 가능

from collections import deque


v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()
# 처음 시작할 때 진입차수가 0 인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
# 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            # 해당 원소와 연결되는 노드들의 진입차수에서 1빼기
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
# 반복이끝나면 위상정렬 수행결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()
