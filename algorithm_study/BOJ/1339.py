# import sys
# input = sys.stdin.readline

# n = int(input())
# alpha = []
# for i in range(65,91):
#     alpha.append(chr(i))
# words = []

# for _ in range(n):
#     a = input()
#     words.append((len(a)-1, a[:len(a)-1]))

# words.sort(reverse=True)
# num = [[] for _ in range(words[0][0])]

# cnt = 10
# for word in words:
#     size, w = word
#     for x in w:
#         num[size-1].append(x)
#         cnt -= 1
#         size -= 1
# result_alpha = []
# result_num = []
# for nu in num:
#     for n in nu:
#         result_alpha.append(n)

# result_alpha.reverse()
# result_a = []
# c = 9
# for alp in result_alpha:
#     for al in alp:
#         if al in alpha:
#             alpha.remove(al)
#             result_a.append(al)
#             result_num.append(str(c))
#             c -= 1

# result = 0
# for word in words:
#     size, wo = word
#     for i in range(len(result_a)):
#         wo = wo.replace(result_a[i], result_num[i])
#     result += int(wo)

# print(result)
import sys
input = sys.stdin.readline

t = int(input())
words = []

for _ in range(t):
    words.append(input())

alphabet = [0 for i in range(26)]

for word in words:
    i = 0
    while word:
        now = word[-1]
        alphabet[ord(now) - ord('A')] += pow(10, i)
        i += 1
        word = word[:-1]

alphabet.sort(reverse=True)
ans = 0
for i in range(9, 0, -1):
    ans += i * alphabet[9 - i]
print(ans)