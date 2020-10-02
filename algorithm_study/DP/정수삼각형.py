# 프로그래머스


# for i in range(len(triangle)):
#     for j in range(len(triangle[i])):
#         print(triangle[i][j])
def solution(triangle):
    for rows in range(1,len(triangle)):
        for i in range(rows+1):
            if i == 0:
                triangle[rows][i] += triangle[rows-1][i]
            elif i == rows:
                triangle[rows][i] += triangle[rows - 1][-1]
            else:
                triangle[rows][i] += max(triangle[rows-1][i-1],triangle[rows-1][i])
        print(triangle[rows])
    return max(triangle[-1])


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))