import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hashmap = {}
for _ in range(n):
    s = input().rstrip()
    if s not in hashmap:
        hashmap[s] = s

cnt = 0
names = []
for _ in range(m):
    s = input().rstrip()
    if s in hashmap:
        names.append(s)
        cnt += 1

names.sort()
print(cnt)
for name in names:
    print(name)