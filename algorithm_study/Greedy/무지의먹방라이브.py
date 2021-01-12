# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1 반환
    if sum(food_times) <= k:
        return -1
    
    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형식으로 우선순위에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기위해 사용할 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식 갯수

    # sum_value + (현재의 음식시간 - 이전 음식 시간) * 현재 음식 개수 와 k비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key= lambda x: x[1])
    return result[(k-sum_value) % length][1]