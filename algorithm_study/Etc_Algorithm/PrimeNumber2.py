# 소수 판별 함수 (시간복잡도 O(X^1/2))
import math


def is_prime_number(x):
    # 2부터 x의 제곱근까지의 수를 확인
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(5))
print(is_prime_number(11))
print(is_prime_number(10))