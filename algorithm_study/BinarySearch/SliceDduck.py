# 떡볶이 떡 만들기
# 파라메트릭 서치 : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법

n, m = map(int, input().split())
dduck = list(map(int, input().split()))
dduck.sort()

start = 0
end = dduck[n-1]
result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in dduck:
        if i > mid:
            total += (i - mid)
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid +1

print(result)