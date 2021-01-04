# 단계별 - 정렬 - 통계학 2108
import sys
from collections import Counter

N = int(sys.stdin.readline())
data = []
sum = 0
for i in range(N):
    data.append(int(sys.stdin.readline()))
    sum += data[i]
data_set = list(set(data))
data = sorted(data)
print(round(sum/N))
print(data[N//2])

# 시간초과 오류 발생한 코드
# cnt_list = []
# for w in data_set:
#     cnt = data.count(w)
#     cnt_list.append(cnt)

# max_list = []
# max_list.append(data_set[cnt_list.index(max(cnt_list))])
# max_list = sorted(max_list)

# if len(max_list) > 1:
#     print(data_set[max_list.index(1)])
# else:
#     print(max_list[0])

cnt_list = Counter(data).most_common() 
#Counter를 사용해 요소의 개수를 셈, most_common()은 빈도수가 높은 순으로 리스트 안의 튜플형태로 반환해줌
# 첫번째와 두번째 value값을 비교해서 같으면 두번째 key값 출력, 다르면 첫번째 key값 출력
if len(cnt_list) > 1: #이 조건문 넣지 않으면 런타임 에러 발생
    if cnt_list[0][1] == cnt_list[1][1]:
        print(cnt_list[1][0])
    else:
        print(cnt_list[0][0])
else:
    print(cnt_list[0][0])
print(max(data)-min(data))
