import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (11)
dp[0] = 1
for i in range(1, 11):
    if i >= 2:
        dp[i] += dp[i-2]
    if i >= 3:
        dp[i] += dp[i-3]
    dp[i] += dp[i-1]

for _ in range(n):
    print(dp[int(input())])