k = 2
score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]

arr = [0] * (len(score))
for i in range(1, len(score)):
    arr[i] = score[i-1] - score[i]

sub_score = set(arr)
sub_arr = [[i,0] for i in sub_score]
for i in range(len(arr)):
    for sub in sub_arr:
        if arr[i] == sub[0]:
            sub[1] += 1
same_num = []
for sub in sub_arr:
    if sub[1] >= k:
        same_num.append(sub[0])
result = []
for same in same_num:
    for i in range(1,len(arr)):
        if arr[i] == same:
            result.append(i-1)
            result.append(i)
result = set(result)
answer = len(score) - len(result)

if answer == 0:
    print("-1")
else:
    print(answer)