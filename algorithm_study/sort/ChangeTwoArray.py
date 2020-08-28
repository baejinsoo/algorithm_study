# 두 배열의 원소 교체
# a,b두 배열은 n개의 원소로 구성됨, k번 원소 교체하여 a배열의 합이 최대가 되게 하자

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    a[i], b[i] = b[i], a[i]

print(sum(a))
