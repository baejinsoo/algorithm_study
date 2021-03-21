import sys
input = sys.stdin.readline

k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))


start = 1
end = sum(data) // n
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for d in data:
        cnt += d // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
