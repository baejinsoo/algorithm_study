# 성적이 낮은 순서로 학생 출력하기

n = int(input())

score_list = []
for i in range(n):
    data = input().split()
    score_list.append((data[0], int(data[1])))

score_list.sort(key=lambda score:score[1])

for i in score_list:
    print(i[0],end=' ')