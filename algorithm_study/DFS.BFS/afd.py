import re


def solution(new_id):
    answer = ''
    for i in new_id:
        if i.isupper():
            j = i.lower()
            new_id = new_id.replace(i, j)
    new_id = re.sub('[^a-z0-9-_.]+', '', new_id)
    for i in range(len(new_id) - 1):
        if new_id[i] == '.':
            if new_id[i + 1] == '.':
                first = ""
                end = ""
                first = new_id[:i] + " "
                end = new_id[i + 1:]
                new_id = first + end
    new_id = new_id.replace(" ", "")

    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:len(new_id) - 1]

    if not new_id:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:len(new_id) - 1]

    if len(new_id) <= 2:
        plus = new_id[-1]
        while len(new_id) < 3:
            new_id = new_id + plus

    print(new_id)
    answer = new_id

    return answer