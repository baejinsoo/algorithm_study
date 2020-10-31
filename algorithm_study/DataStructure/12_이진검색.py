import random

def binSearch(ary, data):
    global count
    pos = -1
    start = 0
    end = len(ary) - 1
    while (start <= end):
        count += 1
        min = (start + end) // 2
        if ary[min] == data:
            return min
        elif ary[min] < data:
            start = min + 1
        else:
            end = min - 1

    return pos



count = 0
dataAry = [ random.randint(100000, 999999) for _ in range(1000000) ]
dataAry.sort()

position = binSearch(dataAry, 111111)
print(position, dataAry[position], '횟수: ', count)

#print(dataAry[:15], dataAry[-10:-1])
