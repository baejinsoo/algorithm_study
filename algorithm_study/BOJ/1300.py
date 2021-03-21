import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
B = []
for i in range(1,n+1):
    for j in range(1,n+1):
        B.append(i * j)

B.sort()
print(B)
