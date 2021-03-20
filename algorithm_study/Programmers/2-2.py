# 프로그램명 길이를 체크하는 함수
def check_len_program(program):
    if 1 <= len(program) <= 10:
        return True
    else:
        return False

# flag_rule명의 길이를 체크하는 함수


def check_len_flag_rule(flag_rule):
    if 0 <= len(flag_rule) <= 99:
        return True
    else:
        return False

# Number가 0~9까지의 숫자인지 체크하는 함수


def check_number(Number):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for Num in Number:
        if Num not in num:
            return False
    return True

# STRING이 알파벳 대소문자로만 이루어져있는지 체크하는 함수


def check_alphabet(STRING):
    for STR in STRING:
        if 65 <= ord(STR) <= 122:
            continue
        else:
            return False
    return True


def solution(program, flag_rules, commands):
    answer = [True] * len(commands)

    # flags를 딕셔너리 형태로 구현해서, 추후 flag를 확장시킬수 잇음
    flags = dict()
    for flag in flag_rules:
        
        flag_name, flag_argument_type = flag.split()
        flags.update({flag_name: flag_argument_type})

    for k in range(len(commands)):
        com = commands[k].split()
        # 프로그램명의 길이 체크
        if not check_len_program(com[0]):
            answer[k] = False
            continue
        # 프로그램명이 다르다면 False 추가하고, 다음 for문으로 continue
        if com[0] != program:
            answer[k] = False
            continue
        # 공백을 제거하고 입력받은 com의 인자를 0번째 프로그램명 이후부터 확인하기위한 ind 선언
        ind = 1
        while 1:
            if ind == len(com):
                break
            # com[ind] 값이 딕셔너리 flags의 key 값에 있다면 value 값에 해당하는 argumet_type 확인
            if com[ind] in flags:
                if flags[com[ind]] == "NULL":
                    if ind == len(com) - 1:
                        # flage_rule의 길이 체크
                        if not check_len_flag_rule(com[ind]):
                            answer[k] = False
                            break
                        answer[k] = True
                        break
                    elif com[ind + 1] not in flags:
                        answer[k] = False
                        break
                    # flag_argument_type이 NULL이라면 flag_rule이 없으므로 다음 ind 확인
                    ind += 1

                elif flags[com[ind]] == "STRING":
                    if ind == len(com)-1:
                        answer[k] = False
                        break
                    elif com[ind+1] not in flags:
                        # flage_rule의 길이 체크
                        if not check_len_flag_rule(com[ind] + com[ind+1]):
                            answer[k] = False
                            break
                        else:
                            # 대소문자의 알파벳으로만 이루어져있는지 확인
                            if not check_alphabet(com[ind+1]):
                                answer[k] = False
                                break
                    # flag_argument_type이 STRING이라면 flag_rule이 있으므로 ind를 하나 건너뛰어서 다음 진행
                    ind += 2

                elif flags[com[ind]] == "STRINGS":
                    if ind == len(com)-1:
                        answer[k] = False
                        break
                    # STRINGS에 해당하는 flag_argument이 몇개 인지 확인하기 위한 cnt변수와 그 내용을 담을 strings 리스트 선언
                    cnt = 1
                    strings = []
                    while ind + cnt < len(com):
                        if com[ind + cnt] not in flags:
                            strings.append(com[ind + cnt])
                            cnt += 1
                        else:
                            break
                    if len(strings) < 1:
                        answer[k] = False
                        break
                    else:
                        # flag_rule 중 길이를 확인하기위한 len_chk 선언
                        len_chk = com[ind]
                        for string in strings:
                            #  flag_argument 해당하는 값이 대소문자의 알파벳으로만 이루어졌는지 체크
                            if not check_alphabet(string):
                                answer[k] = False
                                break
                            len_chk += string
                        # flag_rule의 길이 체크
                        if not check_len_flag_rule(len_chk):
                            answer[k] = False
                            break
                    ind += cnt

                elif flags[com[ind]] == "NUMBER":
                    if ind == len(com)-1:
                        answer[k] = False
                        break
                    elif com[ind+1] not in flags:
                        # flage_rule의 길이 체크
                        if not check_len_flag_rule(com[ind] + com[ind+1]):
                            answer[k] = False
                            break
                        else:
                            # number가 0~9안에 있는지 체크
                            if not check_number(com[ind+1]):
                                answer[k] = False
                                break
                    # flag_argument_type이 NUMBER flag_rule이 있으므로 ind를 하나 건너뛰어서 다음 진행
                    ind += 2

                elif flags[com[ind]] == "NUMBERS":
                    if ind == len(com)-1:
                        answer[k] = False
                        break
                    # STRINGS에 해당하는 flag_argument이 몇개 인지 확인하기 위한 cnt변수와 그 내용을 담을 numbers 리스트 선언
                    cnt = 1
                    numbers = []
                    while ind + cnt < len(com):
                        if com[ind + cnt] not in flags:
                            numbers.append(com[ind + cnt])
                            cnt += 1
                        else:
                            break
                    if len(numbers) < 1:
                        answer[k] = False
                        break
                    else:
                        # flag_rule 중 길이를 확인하기위한 len_chk 선언
                        len_chk = com[ind]
                        for number in numbers:
                            #  flag_argument 해당하는 값이 0~9로 이루어졌는지 체크
                            if not check_number(number):
                                answer[k] = False
                                break
                            len_chk += number
                        # flag_rule의 길이 체크
                        if not check_len_flag_rule(len_chk):
                            answer[k] = False
                            break
                    ind += cnt

            # flag_name이 딕셔너리 flags의 key값에 없다면 False
            else:
                answer[k] = False
                break
    return answer


flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
program = "line"
commands = ["line -n 110 150 -s hi hello zoe -e", "line -n id pwd -n 100"]
print(solution(program, flag_rules, commands))
