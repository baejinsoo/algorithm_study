## 조합을 이용해 푼 방법
from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))
result = set()

# 1,2,3,...n개 의 조합으로 가능한 경우를 set에 넣어감
for i in range(1, n+1):
    sum_coin = list(combinations(coins, i))
    for combi in sum_coin:
        result.add(sum(combi))
print(result)
# 1부터 (전체길이 +1) 까지 set안에 있는지 확인 없으면 출력
res = len(result) + 1
for i in range(1,len(result)+1):
    if i not in result:
        res = i
        print(res)
        break
print(result)
if res > len(result):
    print(res)

# 1원부터 하나씩 금액을 만들 수 있는지 확인하며 증가해 나가는 방식 - Greedy
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for x in data:
#     # 만들 수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x

# print(target)
