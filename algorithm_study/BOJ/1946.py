import sys
input = sys.stdin.readline

m = int(input())
for _ in range(m):
    n = int(input())

    rank = []
    for i in range(n):
        surue, meet = map(int, input().split())
        rank.append((i, surue, meet))

    rank.sort(key=lambda x: x[1])
    cnt = 0
    min_meet = rank[0][2]
    for i in range(1, n):
        if rank[i][2] > min_meet:
            cnt += 1
        min_meet = min(min_meet, rank[i][2])
    print(n - cnt)
