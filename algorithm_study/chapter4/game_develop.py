n, m = map(int,input().split())
x, y, direction = map(int, input().split())

char = [[0]*m for _ in range(n)]
char[x][y] = 1

game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def dir_left():
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3
turn = 0
count = 1

while True:
    print(count, turn)
    dir_left()
    move_x = x + dx[direction]
    move_y = y + dx[direction]
    if game_map[move_x][move_y] == 0 and char[move_x][move_y] == 0:
        char[move_x][move_y] = 1
        count += 1
        x = move_x
        y = move_y
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        move_x = x - dx[direction]
        move_y = y - dy[direction]
        if game_map[move_x][move_y] == 0:
            x = move_x
            y = move_y
        else:
            break
        turn = 0
print(count)


