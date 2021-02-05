n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
positive = []
negative = []
res = 0

for a in arr:
    if a <= 0:
        negative.append(a)
    elif a == 1:
        res += a
    else:
        positive.append(a)

for i in range(len(positive)-1, -1, -2):
    if i - 1 < 0:
        res += positive[0]
    else:
        res += (positive[i] * positive[i-1])

for i in range(0, len(negative), 2):
    if i + 1 >= len(negative):
        res += negative[i]
    else:
        res += (negative[i] * negative[i+1])

print(res)
