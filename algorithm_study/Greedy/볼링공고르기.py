# 조합으로 푼 방법
from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

# 2개를 뽑는 조합 수 구하기
result = list(combinations(balls, 2))
res = set(result)

# 중복되는 무게가 있다면 제거
for i in range(1, m+1):
    if balls.count(i) > 1:
        result.remove((i,i))
# 갯수 출력      
print(len(result))

###
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# # 1부터 10 까지의 무게를 담을 수 있는 리스트
# array = [0] * 11

# for x in data:
#     array[x] += 1

# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m+1):
#     n -= array[i]
#     result += array[i] * n
# print(result)