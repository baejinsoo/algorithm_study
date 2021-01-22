# 백준 11047

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

count = 0
coin.sort(reverse=True)

for c in coin:
    if k // c >= 1:
        count += k // c
        k = k % c
    else:
        continue

print(count)
