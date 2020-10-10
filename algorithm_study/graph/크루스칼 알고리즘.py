# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합찾기
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i
#모든 간선을 담을 리스트와 최종 비용을 담을 변수 선언
edges = []
result = 0

for _ in range(e):
    a,b,cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫번재 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    # 간선을 모두 작은 순부터 모두 확인하면서
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함시켜 비용값에 더해줌
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(cost)
