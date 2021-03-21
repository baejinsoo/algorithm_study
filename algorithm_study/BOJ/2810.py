n = int(input())
seats = input()

if n == 1:
    print(1)

elif n == seats.count('S'):
    print(n)

else:
    res = ['*']
    count = 1
    for i in range(len(seats)):
        if seats[i] == 'S':
            res.append(seats[i])
            res.append('*')
        elif seats[i] == 'L' and count != 2:
            count += 1
            res.append(seats[i])
        elif seats[i] == 'L' and count == 2:
            count = 1
            res.append(seats[i])
            res.append('*')

    print(res.count('*'))
