# S = input()

# result = int(S[0])
# for i in range(1, len(S)):
#     if result == 0:
#         result += int(S[i])
#     elif int(S[i]) == 0 or int(S[i]) == 1:
#         result += int(S[i])
#     else:
#         result *= int(S[i])

# print(result)

### 더 짧아진 코드
s = input()

result = 0
for text in s:
    if result * int(text) == 0:
        result += int(text)
    else:
        result *= int(text)

print(result)