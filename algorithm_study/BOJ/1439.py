s = input()

def make_1(ss):
    res = 0
    check = [s[0]]
    for i in range(1, len(s)):
        if check[-1] != s[i]:
            check.append(s[i])
        else:
            continue
    return check

res = make_1(s)
count_1 = 0
count_0 = 0
for r in res:
    if r == '0':
        count_0 += 1
    else:
        count_1 += 1
print(min(count_0, count_1))
