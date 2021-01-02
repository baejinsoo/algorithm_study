# 단계별 - 재귀 - 10872 팩토리얼

N = int(input())

def factorial(N):
    if N <= 1:
        return N
    return N * factorial(N-1)

print(factorial(N))
