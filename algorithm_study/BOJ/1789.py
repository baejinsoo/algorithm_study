s = int(input())

dp = [0] * 930001
cnt = 0
for i in range(1, 930000):
    cnt += i
    dp[i] = cnt

start = 0
end = 930000

while start <= end:
    mid = (start + end) // 2
    if dp[mid] > s:
        end = mid - 1
    else:
        start = mid + 1

print(end)


"""
5 ~ 7 라인처럼 할게 아니라
수의 합을 구하는 x(x+1)/2 를 이용하는편이 효율이 좋다
s = int(input())
l,r = 1,100000
while l<=r:
    mid = (l+r)//2
    if mid*(mid+1)//2 <= s:
        l = mid+1
    else:
        r = mid
print(r)
"""
