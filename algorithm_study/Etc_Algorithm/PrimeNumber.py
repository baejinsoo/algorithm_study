# 소수 판별 함수
def is_prime_number(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

print(is_prime_number(5))
print(is_prime_number(11))
print(is_prime_number(10))