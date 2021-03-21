import bisect
import sys
input = sys.stdin.readline

x = int(input())
data = list(map(int, input().split()))

dp = []
dp.append(data[0])

for i in range(x):
    print(dp)
    if data[i] > dp[-1]:
        dp.append(data[i])
    else:
        index = bisect.bisect_left(dp, data[i])
        dp[index] = data[i]
print(len(dp))
