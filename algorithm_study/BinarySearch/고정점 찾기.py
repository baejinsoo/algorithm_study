n = int(input())
data = list(map(int, input().split()))
result = 0

for i in range(len(data)):
    if i == data[i]:
        print(i)
        result += 1

if result == 0:
    print(-1)
