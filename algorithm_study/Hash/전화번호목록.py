# 프로그래머스 - Hash 전화번호 목록

# -----------------------------------------------------------------------------------
# 테스트 케이스는 모두 통과하지만 효율성 테스트에서 탈락한 코드
# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             if i == j:
#                 continue
#             elif len(phone_book[i]) < len(phone_book[j]):
#                 if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                     answer = False
#     return answer
# -----------------------------------------------------------------------------------
# from itertools import combinations as c

# def solution(phone_book):
#     answer = True
#     sorted_PB = sorted(phone_book, key=len)
#     for (a, b) in c(sorted_PB, 2):
#         if a == b[:len(a)]:
#             answer = False
#     return answer

# 조합을 사용해 풀어도 효율성 테스트에서 탈락

# -----------------------------------------------------------------------------------
# 해쉬를 사용해 해결
def solution(phone_book):
    answer = True
    hash_pb = {}
    for phone in phone_book:
        hash_pb[phone] = 1

    for phone in phone_book:
        temp = ""
        for num in phone:
            temp += num
            if temp in hash_pb and temp != phone:
                answer = False
    return answer
