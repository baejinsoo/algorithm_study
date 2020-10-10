def check_team(team, x):
    if team[x] != x:
        team[x] = check_team(team, team[x])
    return team[x]


def union_team(team, a, b):
    a = check_team(team, a)
    b = check_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b


N, M = map(int, input().split())
team = [0] * (N + 1)

for i in range(N + 1):
    team[i] = i

for _ in range(M):
    o, a, b = map(int, input().split())
    if o == 0:
        union_team(team,a,b)
    else:
        ac = check_team(team,a)
        bc = check_team(team,b)
        if ac == bc:
            print("YES", end='\n')
        else:
            print("NO", end='\n')
