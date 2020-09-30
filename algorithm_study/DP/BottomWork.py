d = [0] * 1000
n = int(input())

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] * 2

print(d[i] % 796796)
