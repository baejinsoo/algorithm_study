name = "JEROEN"

count = []
for i in range(len(name)):
    count.append(min(ord(name[i]) - ord('A'), 91 - ord(name[i])))

if 0 not in count:
    print(sum(count) + len(count) - 1)
else:
    idx, answer = 0, 0
    while 1:
        answer += count[idx]
        count[idx] = 0
        if sum(count) == 0:
            break
        left, right = 1, 1
        while count[idx-left] == 0:
            left += 1
        while count[idx+right] == 0:
            right += 1
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
    print(answer)
"""
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉통과 (0.01ms, 10.2MB)
테스트 11 〉통과 (0.02ms, 10.1MB)
"""        

"""
# bfs 사용방법 -------------------------------------------------------------
import copy
def solution(name):
    moves = [-1, 1]
    nameList = list(name)
    # start = (nameList, index, count)
    def bfs(start):
        stack = [start]
        
        while stack:
            array, idx, cnt = stack.pop()
            cnt += min(ord(array[idx]) - 65, 91 - ord(array[idx])) # 아스키 코드값으로 변경 횟수 계산
            array[idx] = 'A'
            if array.count('A') == len(array): # 종료 시점
                return cnt
            for move in moves:
                new_array = copy.deepcopy(array) # array 주소 복사 서로 영향 안미치게
                new_idx = idx + move
                new_cnt = cnt + 1
                stack.insert(0, (new_array, new_idx, new_cnt))

    return bfs((nameList, 0, 0))
"""
"""
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.32ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (3.22ms, 10.3MB)
테스트 5 〉	통과 (12.28ms, 10.5MB)
테스트 6 〉	통과 (0.30ms, 10.3MB)
테스트 7 〉	통과 (3.34ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.31ms, 10.4MB)
테스트 10 〉통과 (0.03ms, 10.2MB)
테스트 11 〉통과 (0.36ms, 10.3MB)
"""