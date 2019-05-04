# ##########
# 2016015878 소프트웨어전공 김인영
# 7번째 숙제 6X6 수독 만들기 제출파일 입니다.
# ##########

import random

def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)

    res = []
    res.append(seed)
    res.append(seed[3:] + seed[:3])

    t = [seed[2],seed[0], seed[1], seed[5], seed[3], seed[4]]
    res.append(t)
    res.append(t[3:] + t[:3])

    t = [seed[1], seed[2], seed[0], seed[4], seed[5], seed[3]]
    res.append(t)
    res.append(t[3:] + t[:3])

    return res

def get_integer(message,i,j):
    number = input(message)
    while not (i>=1 and j<=6):
        number = input(message)
    return int(number)

def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level=="하": return 6
    if level == "중": return 8
    if level == "상": return 10

def make_holes(board,no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0,5)
        j = random.randint(0,5)
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes-=1
    return (board, holeset)

def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        print(i,'| ',end="")
        for j in range(len(row)):
            if row[j]==0:
                print(".", "", end="")
            else:
                print(row[j],"",end="")
        i+=1
        print()

def sudokmini():
    solution_board = create_board()

    hole_num = get_level()

    puzzle = []
    for i in solution_board:
        temp = i[:]
        puzzle.append(temp)
    (puzzle_board, res_hole) = make_holes(puzzle, hole_num)

    show_board(puzzle_board)
    while hole_num > 0:
        i = get_integer("가로줄번호(1~6): ",1,6) - 1
        j = get_integer("세로줄번호(1~6): ",1,6) - 1
        if (i, j) not in res_hole:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~6): ",1,6)

        if n == solution_board[i][j]:
            puzzle_board[i][j] = n
            hole_num -= 1
        else:
            print(n, "가 아닙니다. 다시 해보세요.")
        show_board(puzzle_board)
    print("잘 하셨습니다. 또 들려주세요.")

sudokmini()