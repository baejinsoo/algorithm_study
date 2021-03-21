input()
N = map(int, input().split())
input()
M = map(int, input().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1


for m in M:
    if m in hashmap:
        print(1, end=" ")
    else:
        print(0, end=" ")