import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
time = 0
time += arr[0]
for i in range(1, n):
    arr[i] += arr[i-1]
    time += arr[i]

print(time)
