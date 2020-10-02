n = int(input())

d = [5001] * 5001
d[3] = 1
d[5] = 1
for i in range(3,n+1):
    d[i] = min(d[i], d[i-3]+1, d[i-5]+1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])
