def m_sec(time):
    h, m, s = time.split(':')
    return (int(h) * 60 * 60 + int(m) * 60 + int(s))


def m_time(time):
    ans = []
    hour = time // 3600
    h = str(hour).zfill(2)
    min = (time % 3600) // 60
    m = str(min).zfill(2)
    sec = (time % 3600) % 60
    s = str(sec).zfill(2)
    ans.append(h)
    ans.append(m)
    ans.append(s)
    result = ""
    result = ':'.join(ans)

    return result


# play_time="99:59:59"
# adv_time="25:00:00"
# logs=["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
play_time="02:03:55"
adv_time="00:14:15"
logs=["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
ptime = m_sec(play_time)
a = [0] * 400000
s = []

for adv in logs:
    first, second = adv.split('-')
    start = m_sec(first)
    s.append(start)
    end = m_sec(second)
    for i in range(start, end+1):
        a[i] = a[i]+1

if adv_time == play_time:
    # return "00:00:00"
x = m_sec(adv_time)
answer = 400000
temp = 0
for i in s:
    add = 0
    for j in range(i, i+x+1):
        add += a[j]
    if temp < add:
        answer = i
        temp = add
    if temp == add:
        answer = min(answer,i)

result = m_time(answer)
print(result)
