n = int(input())

money = 1000 - n
cnt = 0
changes = [500, 100, 50, 10, 5, 1]

def count(money, change, cnt):
    if money // change > 0:
        cnt += int(money // change)
        money = (money % change)
    return (money, cnt)

for change in changes:
    money, cnt = count(money, change, cnt)

print(cnt)
