# from itertools import combinations
# import sys
# input = sys.stdin.readline

# n = int(input())
# weights = list(map(int, input().split()))
# weights_set = set(weights)

# for i in range(2,n):
#     combi = list(combinations(weights, i))
#     for com in combi:
#         weights_set.add(sum(com))

# weights =list(weights_set)
# for i in range(1, weights[-1]):
#     if i != weights[i-1]:
#         print(i)
#         break

n = int(input())
data = [int(x) for x in input().split()]

data.sort()

num = 1
for d in data:
    if num < d:
        break
    num += d

print(num)
