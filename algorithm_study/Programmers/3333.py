# def solution(enter, leave):
#     answer = [0] * (len(enter)+1)
#     for i in range(len(leave)-1, -1, -1):
#         for chk in enter[enter.index(leave[i])+1:]:
#             if chk in leave[:i+1]:
#                 answer[leave[i]] += 1
#                 answer[chk] += 1

#     for i in range(len(leave)):
#         tmp = leave.index(enter[i])
#         for j in leave[:tmp]:
#             for x in enter[i:enter.index(j)]:
#                 if leave.index(x) > tmp:
#                     answer[i+1] += 1
#                     answer[x] += 1
#     return answer[1:]

def solution(enter, leave):
    answer = [set() for _ in range(len(enter)+1)]
    for i in range(len(leave)-1, -1, -1):
        for chk in enter[enter.index(leave[i])+1:]:
            if chk in leave[:i+1]:
                answer[leave[i]].add(chk)
                answer[chk].add(i+1)
    for i in range(len(leave)):
        tmp = leave.index(enter[i])
        for j in leave[:tmp]:
            for x in enter[i+1:enter.index(j)]:
                if leave.index(x) > tmp:
                    print(x, i+1)
                    answer[enter[i]].add(x)
                    answer[x].add(enter[i])
    result = [0] * len(enter)
    for i in range(1, len(answer)):
        result[i-1] = len(answer[i])
    return result


enter = [3, 2, 1]
leave = [1, 3, 2]

print(solution(enter, leave))
