# 떡볶이 떡 만들기
# 파라메트릭 서치 : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = array[0]
end = array[n-1]
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in array:
        if i > mid:
            total += (i-mid)
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1

print(result, max(array))