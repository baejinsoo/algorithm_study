import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

lis = []
lis.append(data[0])

for i in range(n):
    if data[i] > lis[-1]:
        lis.append(data[i])
    else:
        index = bisect.bisect_left(lis, data[i])
        lis[index] = data[i]

print(len(lis))
for l in lis:
    print(l, end=" ")
