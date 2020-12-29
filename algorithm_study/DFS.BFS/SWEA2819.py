# SW Expert Academy 2819. 격자판의 숫자 이어 붙이기

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def DFS(x, y, s):
    global result
    if len(s) == 7:
        result.add(s)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 4 and 0 <= ny <4:
            DFS(nx, ny, s+array[nx][ny])
            
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    array = [list(input().split()) for _ in range(4)]
    result = set()
    for t in range(4):
        for f in range(4):
            DFS(t, f, array[t][f])
    print('#{} {}'.format(test_case, len(result)))
                     
    # ///////////////////////////////////////////////////////////////////////////////////
