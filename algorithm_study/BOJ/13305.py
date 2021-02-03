# 주유소
import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = int(1e9)
result = 0
for i in range(len(length)):
    if i == 0:
        min_oil = min(min_oil, oil[i])
        result += (length[i] * min_oil)
    else:
        min_oil = min(min_oil, oil[i])
        result += (length[i] * min_oil)
print(result)