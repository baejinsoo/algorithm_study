from collections import deque


n, k = map(int, input().split())
test = []
for i in range(n):
    test.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def check_virus(a,b):
    global s, x, y
    print(test[x-1][y-1])
    while s != 0:
        s -= 1
        if test[a][b] == 0:
            continue
        if test[a][b]:
            temp = test[a][b]
            for i in range(4):
                ax = a + dx[i]
                by = b + dy[i]
                if ax < 0 or ax >= n or by <0 or by >= n:
                    continue
                if test[ax][by] == 0:
                    test[ax][by] = temp
                if test[ax][by] > temp:
                    test[ax][by] = temp
                else:
                    continue
            check_virus(a,b)
    return test[x-1][y-1]


print(check_virus(0,0))
