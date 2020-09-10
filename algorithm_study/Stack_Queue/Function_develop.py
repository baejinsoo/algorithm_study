# 프로그래머스 기능개발
from collections import deque
import math

progresses = [5,5,5]
speeds = [21,25,20]
remain = []
a = []
answer = []
for i in progresses:
    remain.append(100 - int(i))
for i in range(len(remain)):
    date = remain[i] / speeds[i]
    a.append(math.ceil(date))
print(a)
q = deque(a)
first = q.popleft()
x = 1
while q:
    temp = q.popleft()
    if first >= temp:
        x += 1
    else:
        answer.append(x)
        first = temp
        x = 1
answer.append(x)
print(answer)