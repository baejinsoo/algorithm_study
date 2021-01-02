# 단계별 - 브루트포스 - 2580 스도쿠

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
flag = False

def checklist(i, j):
    checking = [1,2,3,4,5,6,7,8,9]

    # 가로 세로 검사
    for k in range(9):
        if sudoku[i][k] in checking:
            checking.remove(sudoku[i][k])
        if sudoku[k][j] in checking:
            checking.remove(sudoku[k][j])
    # 3*3 검사
    i //= 3
    j //= 3
    for p in range(i*3, i*3+3):
        for q in range(j*3, j*3+3):
            if sudoku[p][q] in checking:
                checking.remove(sudoku[p][q])
    # 가능한 숫자로 이루어진 리스트들 리턴
    return checking

def dfs(x):
    global flag

    if flag:
        return
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return
    
    else:
        (i,j) = zeros[x]
        check_list = checklist(i,j)

        for c in check_list:
            sudoku[i][j] = c
            dfs(x+1)
            sudoku[i][j] = 0

dfs(0)
