"""
1번째 푼 방식 : 메모리 초과(sum 2번을 사용하게됨)
data = int(input())

front = []
end = []
data = str(data)
for i in range(len(data)):
    if i < len(data)/2:
        front.append(data[i])
    else:
        end.append(data[i])
sum_f = 0
sum_e = 0
for f in front:
    sum_f += int(f)
for e in end:
    sum_e += int(e)
if sum_e == sum_f:
    print("LUCKY")
else:
    print("READY")
"""
data = input()
length = len(data)
answer = 0
for i in range(length):
    if i < length/2:
        answer += int(data[i])
    else:
        answer -= int(data[i])

if answer == 0:
    print("LUCKY")
else:
    print("READY")