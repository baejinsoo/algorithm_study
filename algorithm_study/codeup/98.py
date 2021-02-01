h, w = map(int, input().split())
n = int(input())

sugar = [[0] * w for _ in range(h)]

for i in range(n):
    l,d,x,y = map(int, input().split())
    x -= 1
    y -= 1
    if d == 0:
        for j in range(l):
            sugar[x][y+j] = 1
    else:
        for j in range(l):
            sugar[x+j][y] = 1

for i in range(h):
    for j in range(w):
        print(sugar[i][j], end=" ")
    print()

