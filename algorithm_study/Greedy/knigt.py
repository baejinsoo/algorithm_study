# n = 8
# chess = [[0]*n for _ in range(n)]
data = input()
row = int(data[1])
column = int(ord(data[0])-96)

steps = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count = 0
for step in steps:
    if (1 <= column + step[0] <= 8) and (1 <= row + step[1] <= 8):
        count += 1
print(count)