# SW Expert Academy 3752. 가능한 시험 점수

# def cal(a, b):
#     global result
#     if b == N:
#         result.add(a)
#         return
#     cal(a + DATA[b], b + 1)
#     cal(a, b + 1)


# T = int(input())
# for test_case in range(1, 1 + T):
#     N = int(input())
#     DATA = list(map(int, input().split()))
#     result = set()
#     cal(0,0)

#     print('#{} {}'.format(test_case, len(result)))

### runtime 에러

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    DATA = list(map(int, input().split()))
    result = set()
    result.add(0)
    for i in range(N):
        temp = []
        for num in result:
            temp.append(DATA[i] + num)
        for t in temp:
            result.add(t)
    print('#{} {}'.format(test_case, len(result)))
