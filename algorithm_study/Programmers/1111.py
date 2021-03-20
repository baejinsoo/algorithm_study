def solution(table, languages, preference):
    answer = ''
    lang = dict()
    for i in range(len(preference)):
        lang.update({languages[i]: preference[i]})

    temp = 0
    for res in table:
        sum_res = 0
        name, l1, l2, l3, l4, l5 = res.split()
        if l1 in lang:
            sum_res += lang[l1] * 5
        if l2 in lang:
            sum_res += lang[l2] * 4
        if l3 in lang:
            sum_res += lang[l3] * 3
        if l4 in lang:
            sum_res += lang[l4] * 2
        if l5 in lang:
            sum_res += lang[l5] * 1
        if temp < sum_res:
            temp = sum_res
            answer = name
        if temp == sum_res:
            tmp = [answer]
            tmp.append(name)
            tmp.sort()
            answer = tmp[0]
        print(name, sum_res)
    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))
