# 백준 11726
import sys
# 파이썬의 재귀 깊이 한계치가 작아서 오류가 발생하기 때문

n = int(input())
d = [0] * 1000
d[1] = 1
d[2] = 2
sys.setrecursionlimit(10**6) # 임의로 한계치를 설정해 주면 문제를 해결

for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2]) % 10007

print(d[n])
