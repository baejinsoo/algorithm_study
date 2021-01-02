# 단계별 - 브루트포스 - 2798 블랙잭

N, M = map(int, input().split())
card = list(map(int, input().split()))

result = 0

for i in range(0,N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = card[i] + card[j] + card[k]
            if result < temp <= M:
                result = temp
print(result)
