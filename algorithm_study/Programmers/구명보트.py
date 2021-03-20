from collections import deque

people = [40, 40, 40, 50, 90]
limit = 100


def solution(people, limit):
    people.sort(reverse=True)
    res = [0] * len(people)
    people = deque(people)
    idx = 0
    res[idx] = people.popleft()
    while people:
        for person in people:
            print(res)
            if res[idx] + person <= limit:
                people.remove(person)
                res[idx] += person
            else:
                idx += 1
                res[idx] += people.pop()
    print(res)
    return idx + 1


print(solution(people, limit))
