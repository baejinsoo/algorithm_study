import sys
input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()

n = len(S)
m = len(P)
arr = [[0] * (n+1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if S[j-1] == P[i-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

answer = []
x = m
y = n
while 1:
    now = arr[x][y]
    if now == 0:
        break
    if arr[x-1][y-1] == (now - 1) and arr[x][y-1] == (now - 1) and arr[x-1][y] == (now-1):
        x -= 1
        y -= 1
        answer.append(S[y])
    else:
        if now == arr[x-1][y]:
            x -= 1
        else:
            y -= 1

print(arr[-1][-1])

if arr[-1][-1] != 0:
    print(''.join(answer[::-1]))
