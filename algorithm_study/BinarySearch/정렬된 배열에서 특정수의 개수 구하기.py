# n개의 원소가 오름차순으로 정렬되어 있다.
# 이때 x가 등장하는 횟수를 계산
import bisect


n, x = map(int, input().split())
data = sorted(list(map(int, input().split())))
count = bisect.bisect_right(data, x) - bisect.bisect_left(data, x)
if count <= 0:
    print(-1)
else:
    print(count)

# -------------------------------------------------------------------------------------
