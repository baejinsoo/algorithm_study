n = int(input())

ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort()
max_weight = ropes[-1]

ropes_count = len(ropes)
for rope in ropes:
    max_weight = max(max_weight, rope * ropes_count)
    ropes_count -= 1

print(max_weight)
