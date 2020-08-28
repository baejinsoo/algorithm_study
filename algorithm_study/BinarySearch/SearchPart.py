# 부품 찾기
# 가게에 부품이 n개가 있다 [8,3,7,9,2]
# 손님이 찾고자 하는 부품 m 개가 있다 [5,7,9]
# 가게에 있으면 yes 없으면 no를 출력

n = int(input())
shop = list(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))
shop.sort()


def search(target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if target == shop[mid] or target == shop[start] or target == shop[end]:
        return mid
    elif target > shop[mid]:
        search(target, mid+1, end)
    else:
        search(target, start, mid-1)


for i in guest:
    result = search(i, 0, n-1)
    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
