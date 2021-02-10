n, k = map(int, input().split())
objs = list(map(int, input().split()))
multi = [0] * n

cnt = 0
temp = 0
res = 0
for i in range(k):
    if objs[i] in multi:
        continue
    elif 0 in multi:
        multi[multi.index(0)] = objs[i]
    else:
        for m in multi:
            if m not in objs[i:]:
                temp = m
                break
            elif objs[i:].index(m) > cnt:
                cnt = objs[i:].index(m)
                temp = m
        multi[multi.index(temp)] = objs[i]
        temp =  0
        cnt = 0
        res += 1

print(res)