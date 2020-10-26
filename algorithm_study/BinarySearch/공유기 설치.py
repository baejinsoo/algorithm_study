# BOJ 2110
def near_value(data, x):
    for s in range(1, x+1):
        if x+s in data:
            return x+s
        elif x-s in data:
            return x-s


n, c = map(int, input().split())
data = []
for _ in range(n):
    d = int(input())
    data.append(d)

data.sort()
share = [data[0], data[-1]]
c -= 2

x = int(data[0] + data[-1] / (c + 1))
for i in range(1, c+1):
    if x*i in data:
        share.append(x*i)
    else:
        value = near_value(data, x)
        share.append(value)

share.sort()
result = n
for i in range(1, len(share)):
    result = min(result, share[i] - share[i-1])
print(result)
print(share)

