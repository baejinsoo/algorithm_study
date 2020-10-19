s = input()
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
num = []
cha = []

for i in s:
    if i in a:
        num.append(i)
    else:
        cha.append(i)

num_sum = 0
for n in num:
    num_sum += int(n)
cha_sort = ''.join(sorted(cha))
cha_sort = cha_sort + str(num_sum)

print(cha_sort)
