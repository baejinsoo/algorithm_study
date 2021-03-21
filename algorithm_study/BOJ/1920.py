import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))


def find(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


a.sort()
for i in b:
    if find(a, i, 0, n-1):
        print(1)
    else:
        print(0)
