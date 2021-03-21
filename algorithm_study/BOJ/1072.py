import sys
import math
input = sys.stdin.readline

x, y = map(int, input().split())
z = math.floor((y / x) * 100)
start = 1
end = 1e9
answer = -1

while start <= end:
    mid = (start + end) // 2
    dx = x + mid
    dy = y + mid
    dz = math.floor((dy / dx) * 100)
    if z < dz:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

if z >= 99:
    print(-1)
else:
    print(math.floor(answer))
