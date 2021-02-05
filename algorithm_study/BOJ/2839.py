# INF = int(1e9)
# n = int(input())

# d = [INF] * 5001
# d[3] = 1
# d[5] = 1
# for i in range(3, n+1):
#     d[i] = min(d[i], d[i-3] + 1, d[i-5]+1)

# if d[n] == INF:
#     print(-1)
# else:
#     print(d[n])

# 2839 설탕 배달 그리디

n = int(input())
c = 0

while True:
    if n % 5 != 0:
        if n == 1 or n == 2:
            c = -1
            break
        else:
            n -= 3
            c += 1
    elif n % 5 == 0:        
        c += (n // 5)
        break

print(c)