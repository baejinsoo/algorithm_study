import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * m for _ in range(n)]
B = [[0] * m for _ in range(n)]
for i in range(n):
    input_list = str(input())
    for j in range(m):
        A[i][j] = int(input_list[j])

for i in range(n):
    input_list = str(input())
    for j in range(m):
        B[i][j] = int(input_list[j])


def change(A, x, y):
    for i in range(3):
        for j in range(3):
            if A[x+i][y+j] == 1:
                A[x+i][y+j] = 0
            else:
                A[x+i][y+j] = 1


cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            change(A, i, j)
            cnt += 1
        else:
            continue

if A == B:
    print(cnt)
else:
    print(-1)
