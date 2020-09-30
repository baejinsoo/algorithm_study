numbers = [2,4,3,1,3,1]
answer = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        answer.append(numbers[i]+numbers[j])
        print(answer)
a = set(answer)
answer = list(a)
answer.sort()
print(answer)
