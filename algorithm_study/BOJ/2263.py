import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0] * (n+1)
for i in range(n):
    position[inorder[i]] = i

preorder = []

def divide(in_le, in_ri, po_le, po_ri):
    if in_le > in_ri or po_le > po_ri:
        return
    
    parent = postorder[po_ri]
    print(parent, end=" ")

    left = position[parent] - in_le # 왼쪽 갯수
    right = in_ri - position[parent] # 오른쪽 갯수

    divide(in_le, in_le + left -1, po_le, po_le + left - 1)
    divide(in_ri - right + 1, in_ri, po_ri - right, po_ri -1)

divide(0, n-1, 0, n-1)
