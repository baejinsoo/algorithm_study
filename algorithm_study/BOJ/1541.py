# 문제를 완전히 잘못 이해해서 산으로 가게 푼 문제....
# sik = input()
# number = ['0','1','2','3','4','5','6','7','8','9']

# res = []
# n = ""
# sik = sik.replace("(-","(")
# for s in sik:
#     if s in number:
#         n += s
#     elif s == '(':
#         n += '-'
#     else:
#         if n:
#             res.append(int(n))
#         n = ""
# res.append(int(n))
# result = 0
# for i in range(len(res)):
#     if i == 0:
#         result += res[i]
#     elif res[i] > 0:
#         result -= res[i]
#     else:
#         result += res[i]
# print(result)

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)