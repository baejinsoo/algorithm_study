"""
n = 3
lost =[3]
reserve = [1]
"""
def solution(n, lost, reverse):
    res = (n - len(lost))
    lost.sort()
    reserve.sort()

    cal = [-1, 1]

    for re in reserve:
        for i in range(2):
            check = re + cal[i]
            if 0 < check <= n and check in lost:
                res += 1
                lost.remove(check)
                break
    return(res)

n = 5
lost =[2,3]
reserve = [1,3]
print(solution(n, lost, reserve))


# def solution(n, lost, reverse):
#     student=[1]*n
#     for i in reverse:
#         student[i-1] +=1
#     for i in lost:
#         student[i-1] -=1
#     for i in range(1,len(student)):
#         if student[i] == 0 and student[i-1] == 2:
#             student[i] += 1
#             student[i-1] -= 1
#     for i in range(len(student)-1):
#         if student[i] == 0 and student[i+1] == 2:
#             student[i] += 1
#             student[i+1] -= 1
#     student2 = [i for i in student if i>0]
#     result = len(student2) 
#     return result