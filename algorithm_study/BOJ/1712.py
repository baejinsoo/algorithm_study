# 단계별 - 수학문제 - 1712 손익분기점

A, B, C = map(int, input().split())
result = 1
if C <= B:
    print(-1)
elif A < (C-B)*result:
    print(result)
else:
    print(int(A/(C - B)) + 1)
