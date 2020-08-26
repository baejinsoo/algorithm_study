# dfs 이용
# 프로그래머스 dfs level2
def solution(numbers, target):
    result_list = [0]
    # [-1,1] [-2,0,0,2],[-3,-1,-1,1,-1,1,1,3] ... numbers의 원소들을 하나씩 더하고 빼기를 저장

    for i in range(len(numbers)):
        temp_list = []
        for j in range(len(result_list)):
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        result_list = temp_list
    return result_list.count(target)

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))