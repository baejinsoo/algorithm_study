#  에라토스테네스의 체
# 1. 2 부터 N까지의 모든 자연수 나열
# 2. 남은 수중 아직 처리하지 않은 가장 작은 수 i 찾아서 배수들 모두 제거과정 반복

import math

n = 1000
# 초기에 모든 수가 소수(True)인 것으로 초기화 (0, 1제외)
array = [True for i in range(n+1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        # i가 소수인경우 i를 제외한 i의 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')