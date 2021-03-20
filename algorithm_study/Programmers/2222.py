upper = []
lower = []
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sign = ['~', '!', '@', '#', '$', '%', '^', '&', '*']
for i in range(65, 91):
    upper.append(chr(i))
    lower.append(chr(i+32))


def check_1(inp_str):
    if 8 <= len(inp_str) <= 15:
        return True
    else:
        return False


def check_2(inp_str):
    chk = True
    for inp in inp_str:
        if inp not in number:
            if inp not in sign:
                if inp not in upper:
                    if inp not in lower:
                        chk = False
    return chk


def check_3(inp_str):
    chk = [False, False, False, False]
    for inp in inp_str:
        if inp in number:
            chk[0] = True
        elif inp in sign:
            chk[1] = True
        elif inp in upper:
            chk[2] = True
        elif inp in lower:
            chk[3] = True
    res = 0
    for c in chk:
        if c:
            res += 1
    if res >= 3:
        return True
    else:
        return False


def check_4(inp_str):
    chk = []
    for inp in inp_str:
        chk.append(ord(inp))
    chk_num = 1
    for i in range(1, len(chk)):
        if chk_num >= 4:
            return False
        if chk[i-1] == chk[i]:
            chk_num += 1
        else:
            chk_num = 1
    if chk_num >= 4:
        return False
    else:
        return True


def check_5(inp_str):
    chk = []
    for inp in inp_str:
        chk.append(ord(inp))
    tmp_chk = set(chk)
    for tmp in tmp_chk:
        if chk.count(tmp) >= 5:
            return False
    return True


def solution(inp_str):
    answer = []
    if not check_1(inp_str):
        answer.append(1)
    if not check_2(inp_str):
        answer.append(2)
    if not check_3(inp_str):
        answer.append(3)
    if not check_4(inp_str):
        answer.append(4)
    if not check_5(inp_str):
        answer.append(5)
    if not answer:
        answer.append(0)
    return answer


inp_str = "::::::::"
print(solution(inp_str))
