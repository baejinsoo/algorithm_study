go = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def ten(x, y):
    global go
    for i in range(4):
        count = 1
        nx, ny = x, y
        while 0 < nx < 18 and 0 < ny < 18:
            # print(nx, ny)
            nx = x + dx[i] * count
            ny = y + dy[i] * count
            if go[nx][ny] == 0:
                go[nx][ny] = 1
            elif go[nx][ny] == 1:
                go[nx][ny] = 0
            count += 1
        

for i in range(19):
    go_x = list(map(int, input().split()))
    go.append(go_x)

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    ten(x-1,y-1)


for i in range(19):
    for j in range(19):
        print(go[i][j], end=" ")
    print()
    