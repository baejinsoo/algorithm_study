import sys
input = sys.stdin.readline

n = int(input())
bugets = list(map(int, input().split()))
m = int(input())
bugets.sort()
start = 0
end = bugets[-1]

answer = 0
while start <= end:
    mid = (start + end) // 2
    res = 0
    for buget in bugets:
        if buget <= mid:
            res += buget
        else:
            res += mid
    if res > m:
        end = mid - 1
    elif res < m:
        start = mid + 1
        answer = max(answer, mid)
    elif res == m:
        answer = mid
        break

print(answer)
