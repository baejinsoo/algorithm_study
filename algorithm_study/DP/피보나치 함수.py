N = int(input())


fibo_list = [[0 for _ in range(2)] for _ in range(41)]

fibo_list[0] = [1,0]
fibo_list[1] = [0,1]
for i in range(2,41):
    fibo_list[i][0] = fibo_list[i-1][0] + fibo_list[i-2][0]
    fibo_list[i][1] = fibo_list[i-1][1] + fibo_list[i-2][1]

for i in range(N):
    n = int(input())
    print(fibo_list[n][0], fibo_list[n][1])
