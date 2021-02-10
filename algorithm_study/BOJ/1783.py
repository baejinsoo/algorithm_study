n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m+1)//2))
else:
    if m <= 6:
        print(min(4,m))
    else:
        print(m-2)

# https://lipcoder.tistory.com/entry/%EB%B3%91%EB%93%A0-%EB%82%98%EC%9D%B4%ED%8A%B8-%EB%B0%B1%EC%A4%80-1783%EB%B2%88