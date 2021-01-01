# 단계별 - 문자열 - 1157 단어공부

word = input()
word = word.upper()
# 딕셔너리 형태로 풀었으나 런타임 에러 발생
# word_dict = {}
# for w in word:
#     if w in word_dict:
#         word_dict[w] += 1
#     else:
#         word_dict[w] = 1

# sort_dict = sorted(word_dict.items(), key=lambda x:x[1], reverse=True)
# print(sort_dict,sort_dict[0][1], sort_dict[1][1])

# if sort_dict[0][1] == sort_dict[1][1]:
#     print('?')
# if sort_dict[0][1] != sort_dict[1][1]:
#     print(sort_dict[0][0])

unique_word = list(set(word))
cnt_list = []
for w in unique_word:
    cnt = word.count(w)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(unique_word[cnt_list.index(max(cnt_list))])