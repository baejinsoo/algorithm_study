# 소수 판별 함수 (시간복잡도 O(X^1/2))
# import math
#
#
# def is_prime_number(x):
#     # 2부터 x의 제곱근까지의 수를 확인
#     for i in range(2,int(math.sqrt(x))+1):
#         if x % i == 0:
#             return False
#     return True
#
# print(is_prime_number(5))
# print(is_prime_number(11))
# print(is_prime_number(10))

arr = [-5,4,-2,3,1,-1,-6,-1,0,5]
    # Write your code here

result = 1
x = 1
for i in arr:
    if result + i < 1:
        while result + i < 1:
            x += 1
            result += 1
        result = 1
    else:
        result += i
    print(i, x, result)
print(x)

