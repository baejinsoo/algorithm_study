# 단계별 - 배열 - 4344 평균은 넘겠지

N = int(input())

for i in range(N):
    array = list(map(int, input().split()))
    sum = 0
    num = 0
    for arr in array[1:]:
        sum += arr
    result = float(sum/array[0])
    for arr in array[1:]:
        if arr > result:
            num += 1
    print("{0:.3f}%".format(float(num/array[0])*100))

    ## 소수점 세번째 자리까지 표시법
    # 1. round(n,3) => 소수자리가 0이면 출력을 안함
    # 2. format 사용 => {0:.3f}
