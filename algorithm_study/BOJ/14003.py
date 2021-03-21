import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

lis = []
lis.append(data[0])
record = [0] * n

for i in range(n):
    if data[i] > lis[-1]:
        lis.append(data[i])
        record[i] = len(lis) - 1
    else:
        index = bisect.bisect_left(lis, data[i])
        lis[index] = data[i]
        record[i] = index

result = len(lis)
print(result)
answer = []
result -= 1
for i in range(n-1, -1, -1):
    if result == record[i]:
        answer.append(data[i])
        result -= 1

answer.reverse()
print(*answer)
