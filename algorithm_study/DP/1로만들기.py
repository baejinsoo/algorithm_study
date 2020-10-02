n = int(input())

d = [0] * 1000001

for i in range(1, n+1):
    d[i] = d[i-1] + 1
    d[1] = 0
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[i])
