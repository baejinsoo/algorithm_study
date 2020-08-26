# 프로그래머스 level 3
def dfs(network,visited,x):
    if visited[x] == 0:
        visited[x] = 1
    for i in range(len(network)):
        if network[x][i] == 1 and visited[i]==0:
            dfs(network,visited,i)


def solution(n,network):
    count = 0
    visited = [0]*n
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                dfs(network,visited,i)
                count += 1
    return count


n = int(input())
network = []
network = [list(map(int,input().split(','))) for _ in range(n)]
print(solution(n, network))
