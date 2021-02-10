import sys
input = sys.stdin.readline

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))

scores.reverse()
check = scores[0]
cnt = 0
for i in range(1, len(scores)):
    while check <= scores[i]:
        cnt += 1
        scores[i] -= 1
    check = scores[i]

print(cnt)