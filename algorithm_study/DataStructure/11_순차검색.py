import random
# 중복된 데이터가 없다고 가정
# (1) 해당 값이 1개만 있다
# (2) 1개만 찾으면 된다
def seqSearch(ary, data):
    pos = -1

    for i in range(len(ary)):
        if ary[i] == data:
            pos = i
            break
    return pos

# 중복된 값을 모두 찾을때
def seqSearchMulti(ary, data):
    pAry = []
    for i in range(len(ary)):
        if (ary[i] == data):
            pAry.append(i)
    return pAry

dataAry = [ random.randint(11, 99) for _ in range(200) ]
print(dataAry)

pos = seqSearch(dataAry, 99)
print(pos)
posAry = seqSearchMulti(dataAry, 50)
print(posAry)
