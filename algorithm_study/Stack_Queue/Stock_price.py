# 프로그래머스 > 스택/큐 > 주식가격
from collections import deque

prices = [1,2,3,2,3]
answer = [0]*5


def solution(prices):
    answer = []
    for i in range(len(prices)):
        num = 0
        for j in range(i+1, len(prices)):
            num += 1
            if prices[i] > prices[j]:
                break
        answer.append(num)
    return answer


