# 백준 1181 단어정렬

n = int(input())
sort_word = {input() for _ in range(n)}
sort_word = list(sort_word)
# 단어크기 우선정렬 같으면 알파벳 순으로 정렬
sort_word.sort(key= lambda word: (len(word),word))

for i in sort_word:
    print(i)
