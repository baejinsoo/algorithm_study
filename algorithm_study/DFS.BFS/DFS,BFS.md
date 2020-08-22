### DFS / BFS

##### stack

-  선입선후출
- list로 스택 구현

```python
stack = []
stack.append(5)
stack.append(3)
stack.append(6)
stack.pop()

print(stack[::-1]) #최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```

##### Queue

- 선입선출(은행창구)

```python
from collections import deque
# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(4)
queue.append(2)
queue.popleft()
queue.append(3)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() #역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

##### 재귀함수

- 자기 자신을 다시 호출하는 함수(스택과 유사)

```python
def recursive_function():
	print('재귀 함수 호출')
	recursive_function()
	
recursive_function()
```

###### 재귀함수 종료조건 명시

```python
def recursive_function(i):
    # 100번째 호출 했을 때 종료
    if i == 100:
        return
	print(i,'재귀 함수 호출')
	recursive_function(i+1)
	
recursive_function(1)
```

#### DFS(Depth-First-Search)

- 깊이 우선탐색
- 스택 자료구조(혹은 재귀함수)
  - 탐색 시작 노드를 스택에 삽입하고 방문 처리
  - 스택의 최상단 노드에 바웅 접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리, 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
  - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

```python
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = '')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
```

#### BFS(Breath-Frist Search)

- 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색
- 큐 자료구조
  - 탐색 시작 노드를 큐에 삽입하고 방문처리
  - 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
  - 더 이상 수행할 수 없을 때까지 반복

```python
from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```



