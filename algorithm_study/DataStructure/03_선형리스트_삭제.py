katok = ['다현','정연','쯔위','시나','지효',]


def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])

delete_data(2)
print(katok)

delete_data(1)
print(katok)
