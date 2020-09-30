def solution(N, number):
    array = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        set_num = []
        set_num.append(int(str(N)*i))
        for i_half in range(1, i // 2 + 1):
            for j in array[i_half]:
                for k in array[i - i_half]:
                    set_num.append(j+k)
                    set_num.append(j-k)
                    set_num.append(k-j)
                    set_num.append(k*j)
                    if k != 0:
                        set_num.append(j/k)
                    if j != 0:
                        set_num.append(k/j)
            if number in set_num:
                return i
            array.append(set_num)
    return -1

N = 5
number = 12
print(solution(N,number))

