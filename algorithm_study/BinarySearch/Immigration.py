# 프로그래머스 입국심사

def solution(n, times):
    # 배열 정렬
    times.sort()
    left = 0
    # 최대값으로 가장 오래걸리는 경우입력
    right = int(times[len(times)-1]) * n
    answer = right
    while right >= left:
        mid = int((right+left)//2)
        people = 0
        for i in times:
            people += mid//i
        if people>=n:
            # n과 people 값이 같아도 시간의 최솟값이 나올때까지 반복
            if answer > mid:
                answer = mid
            right = mid -1
        else:
            left = mid+1
    return answer
