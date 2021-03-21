from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
data = list(map(int, input().split()))

cards.sort()
for d in data:
    a = bisect_left(cards, d)
    b = bisect_right(cards, d)
    print(b-a, end=" ")


"""
해쉬 사용방법

input()
N = map(int,input().split())
input()
M = map(int,input().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))