katok = ['다현','정연','쯔위','시나','지효',]


def insert_data(position, friend):
    katok.append(None) # 빈칸 추가
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend


insert_data(2, '솔라')
print(katok)
insert_data(3, '재남')
print(katok)
