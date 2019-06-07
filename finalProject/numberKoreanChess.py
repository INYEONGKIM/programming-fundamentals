import random

C_END = "\033[0m"
C_BOLD = "\033[1m"

C_RED = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_CYAN = "\033[36m"


class chessPieces:
    def __init__(self, visible, value, team):
        self.visible = visible
        self.value = value
        self.team = team

def initBoard():
    # K = king, M = mine, S = space
    mainBoard = []
    computerPieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "M", "M", "M", "S", "S", "S", "S"]
    playerPieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "M", "M", "M", "S", "S", "S", "S"]

    random.shuffle(computerPieces)
    s = ""
    isRandom = False
    while not (s == "Y" or s == "y" or s == "N" or s == "n"):
        s = input("말 배치를 무작위로 하시겠습니까?(y/n) : ")

    if s == "Y" or s == "y":
        isRandom = True

    # 말 배치 사용자 임의 지정
    else:
        # INYEONG
        personalList = []
        possibleList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "M", "M", "M", "S", "S", "S", "S"]
        print(C_BOLD + C_CYAN + "[SYSTEM] : 원하는 다음과 같은 형식에 맞추어 입력해 주세요! 왕 : K, 지뢰 : M, 공백 : S, 그 외 말 : 숫자")
        print("     예시 : 1 2 3 S K 10"+ C_END)

        quitFlag = False
        for k in range(3):
            while True:
                if quitFlag:
                    break
                print("\n입력 가능한 말 목록 ", possibleList)
                print(C_BOLD + C_YELLOW + "[SYSTEM] : ", end="")
                if k==0:
                    print("가장 전방에 ", end="")
                elif k==1:
                    print("가운대 줄에 ", end="")
                else:
                    print("마지막 줄에 ", end="")
                print("배치할 말 6개를 입력해 주세요! (갑자기 귀찮아 졌다면 : q, 무작위 배치됩니다.) " + C_END, end="")
                rawData = input().strip().upper()

                if rawData == "Q":
                    isRandom = True
                    quitFlag = True
                    break

                rawSplit = rawData.split()
                if len(rawSplit) == 6:
                    numberTemp = []
                    strTemp = []
                    mCnt = 0
                    sCnt = 0
                    kCnt = 0

                    tmCnt = 0
                    tsCnt = 0
                    tkCnt = 0
                    for i in possibleList:
                        if i=="S":
                            sCnt+=1
                        elif i=="M":
                            mCnt+=1
                        elif i=="K":
                            kCnt+=1

                    breakFlag = False
                    for i in rawSplit:
                        if i=="K" or i=="S" or i=="M" or (len(i)==2 and i=="10") or (len(i) == 1 and 1 <= ord(i)-ord('0') <= 9):
                            if i!="K" and i!="S" and i!="M":
                                i = int(i)
                                if i not in possibleList:
                                    print("[SYSTEM] : 해당 숫자는 이미 사용했습니다! [ERROR] : " + str(i))
                                    break
                                else:
                                    numberTemp.append(i)
                            else:
                                if i=="S":
                                    tsCnt+=1
                                elif i=="M":
                                    tmCnt+=1
                                elif i=="K":
                                    tkCnt+=1
                                strTemp.append(i)
                        else:
                            print("[SYSTEM] : 올바르지 않은 입력이 있습니다! [ERROR] : " + i)
                            breakFlag = True
                            break

                    numberTempSet = set(numberTemp)
                    if len(numberTempSet) + len(strTemp) != 6:  # found duplicate
                        if not breakFlag:
                            print("[SYSTEM] : 같은 숫자를 여러번 사용할 수 없습니다!")
                        continue
                    elif tsCnt > sCnt:
                        print("[SYSTEM] : 너무 많은 공백을 배치했습니다!")
                        continue
                    elif tmCnt > mCnt:
                        print("[SYSTEM] : 너무 많은 지뢰를 배치했습니다!")
                        continue
                    elif tkCnt > kCnt:
                        print("[SYSTEM] : 너무 많은 왕을 배치했습니다!")
                        continue
                    else:
                        # success
                        for i in rawSplit:
                            if i != "K" and i != "S" and i != "M":
                                i = int(i)
                            personalList.append(i)
                            possibleList.remove(i)
                        print(C_BOLD + C_RED + "[SYSTEM] : 한 줄 추가를 완료했습니다!" + C_END)
                        break
                else:
                    print("[SYSTEM] : 6개를 올바르게 입력하지 않았습니다!")

    for i in range(9):
        # computer pieces setting
        if 0 <= i <= 2:
            mainBoard.append([])
            for j in range(6):
                temp, computerPieces = computerPieces[0], computerPieces[1:]
                if temp != "S":
                    # False 로 바꾸기
                    mainBoard[i].append(chessPieces(False, temp, "Computer"))
                else:
                    mainBoard[i].append(chessPieces(True, temp, "none"))

        # space pieces setting
        elif 3 <= i <= 5:
            mainBoard.append([chessPieces(True, "S", "none")] * 6)

        # player pieces setting
        else:
            if isRandom:
                random.shuffle(playerPieces)
                mainBoard.append([])
                for j in range(6):
                    temp, playerPieces = playerPieces[0], playerPieces[1:]
                    if temp != "S":
                        mainBoard[i].append(chessPieces(True, temp, "Player"))
                    else:
                        mainBoard[i].append(chessPieces(True, temp, "none"))
            else:
                # 사용자 정의 배치
                mainBoard.append([])
                for j in range(6):
                    temp, personalList = personalList[0], personalList[1:]
                    if temp != "S":
                        mainBoard[i].append(chessPieces(True, temp, "Player"))
                    else:
                        mainBoard[i].append(chessPieces(True, temp, "none"))

    return mainBoard


def printBorad(board, playerLeftPieces, computerLeftPieces):
    # Print Grid
    print(C_BOLD + C_YELLOW + "  | " + C_END, end="")
    print(C_BOLD + C_GREEN + "0   1\t" + C_END, end="")
    print(C_BOLD + C_RED + "|\t" + C_END, end="")
    print(C_BOLD + C_GREEN + "2   3   " + C_END, end="")
    print(C_BOLD + C_RED + "|\t" + C_END, end="")
    print(C_BOLD + C_GREEN + "4   5   " + C_END)
    print(C_BOLD + C_YELLOW + "----------------------------------   " + C_END, end="")
    print(C_BOLD + C_YELLOW + "남은 CPU 말\t\t: ", end="")
    for i in computerLeftPieces:
        print(str(i) + " ", end="")
    print(C_END)

    for i in range(9):
        print(C_BOLD + C_GREEN + str(i) + C_END, end="")
        print(C_BOLD + C_YELLOW + " | " + C_END, end="")
        for j in range(6):
            if not board[i][j].visible:
                print(C_BOLD + C_RED + "?" + C_END + "\t", end="")
            else:
                if not board[i][j].value == "S":
                    if board[i][j].team == "Player":
                        print(C_BOLD + C_CYAN + str(board[i][j].value) + C_END + "\t", end="")
                    else:
                        print(C_BOLD + C_RED + str(board[i][j].value) + C_END + "\t", end="")
                else:
                    print(str(board[i][j].value) + "\t", end="")
            if j % 2 == 1 and not j == 5:
                print(C_BOLD + C_RED + "|\t" + C_END, end="")
        if i == 8:
            print(C_BOLD + C_YELLOW + "남은 Player 말\t: ", end="")
            for i in playerLeftPieces:
                print(str(i) + " ", end="")
            print(C_END)
        else:
            print()


def checkEndListCondition(player, computer):
    if 'K' not in player:
        print("[SYSTEM] : Player's king is dead")
        return True, "Computer"

    if 'K' not in computer:
        print("[SYSTEM] : Computer's king is dead")
        return True, "Player"

    # 왕 빼고 모든 말이 죽은 경우
    if len(player) == 1:
        return True, "Computer"

    if len(computer) == 1:
        return True, "Player"

    return False, None


def checkEndBoardCondition(board):
    for i in range(6):
        if board[0][i].team == "Player" and board[0][i].value == "K":
            return True, "Player"

        if board[8][i].team == "Computer" and board[8][i].value == "K":
            return True, "Computer"

    return False, None


# 입력이 정수인지 확인하는 함수
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# player part
def playerPart(board, playerLeftPieces, computerLeftPieces):
    print("Player 차례")
    l = ['a', 'q', 'w', 'ww', 'e', 'd']
    x = 100
    y = 100
    # 움직일 말 선택
    while True:
        while True:
            marker = input("말을 선택 하세요(왕은 K 입력) ").upper()
            if marker == 'K':
                break
            elif isNumber(marker):
                if 1 <= int(marker) <= 10 and int(marker) in playerLeftPieces:
                    marker = int(marker)
                    break
                else:
                    continue
            else:
                continue
        # 말 좌표 찾기
        for i in range(9):
            for j in range(6):
                if (board[i][j].team == "Player") and (marker == board[i][j].value):
                    x, y = i, j

        print("↑ : w (2칸 가려면 ww)\n← : a\n→ : d\n↖ : q\n↗ : e")
        while True:
            direction = input("방향 선택 해 주세요 ")
            if direction in l:
                break

        # 말 옮기기
        try:
            if direction == 'a' and y - 1 >= 0 and board[x][y - 1].value == "S":  # to the left
                board[x][y - 1] = board[x][y]
                board[x][y] = chessPieces(True, "S", "none")
                y -= 1
                break
            elif direction == 'd' and y + 1 < 6 and board[x][y + 1].value == "S":  # to the right
                board[x][y + 1] = board[x][y]
                board[x][y] = chessPieces(True, "S", "none")
                y += 1
                break
            elif (direction == 'w' and x - 1 >= 0 and board[x - 1][y].value == "S"):  # to the forward 1
                board[x - 1][y] = board[x][y]
                board[x][y] = chessPieces(True, "S", "none")
                x -= 1
                break
            elif (direction == 'ww' and x - 2 >= 0 and board[x - 2][y].value == "S" and board[x - 1][
                y].value == "S"):  # to the forward 2
                board[x - 2][y] = board[x][y]
                board[x][y] = chessPieces(True, "S", "none")
                x -= 2
                break
            elif (direction == 'q' and x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1].value == "S"):  # 왼대각
                board[x - 1][y - 1] = board[x][y]
                board[x][y] = chessPieces(True, "S", "none")
                x -= 1
                y -= 1
                break
            elif (direction == 'e' and x - 1 >= 0 and y + 1 < 6 and board[x - 1][y + 1].value == "S"):  # 오대각
                board[x - 1][y + 1] = board[x][y]
                board[x][y] = chessPieces(True, "S", "none")
                x -= 1
                y += 1
                break
            else:
                print("불가능한 움직임 입니다. 다시 선택해 주세요")
                continue
        except IndexError:
            print("다시 선택해 주세요")

    # Player Battle
    board, playerLeftPieces, computerLeftPieces = playerBattle(board, playerLeftPieces, computerLeftPieces, x, y, board[x][y].value)

    # Player revive
    # BAEK
    if (x + 1 == 1 and (direction == "e" or direction == "q" or direction == "w")) or (
            x + 2 == 2 and (direction == "ww")):  # reach end
        rescuablePieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in playerLeftPieces:  # set possible pieces
            if type(i) == int:
                rescuablePieces.remove(i)
        if rescuablePieces == []:
            print("[SYSTEM] : 부활에 실패했습니다. 살릴 수 있는 말이 없습니다.")
        else:
            possibleIndex = [0, 1, 2, 3, 4, 5]
            for i in range(6):
                if board[8][i].value != "S":  # Player 0번줄의 공백여부 판단
                    possibleIndex.remove(i)
            if possibleIndex == []:
                print("[SYSTEM] : 부활에 실패했습니다. Player의 첫 번째 줄이 가득찼습니다.")
            else:
                while True:
                    try:
                        revive_pin = int(input("[SYSTEM] : 부활시킬 말을 입력하세요 : "))
                        if (type(rescuablePieces.index(revive_pin)) == int):
                            break
                    except ValueError :
                        print("[SYSTEM] : 살릴 수 있는 말이 아닙니다.")
                        continue

                while True:
                    try:
                        revive_point = int(input("[SYSTEM] : 부활할 자리의 y좌표를 입력하세요 : "))
                        if (type(possibleIndex.index(revive_point)) == int):
                            break
                    except ValueError :
                        print("[SYSTEM] : 자리에 뭔가 있습니다! ")
                        continue
                print("[SYSTME] : 영웅은 죽지 않아요! (0, " + str(revive_point) + ")에 " + str(
                    revive_pin) + "이/가 부활했습니다!")
                board[8][revive_point] = chessPieces(True, revive_pin, "Player")
                playerLeftPieces.append(revive_pin)

    return board, playerLeftPieces, computerLeftPieces


# INYEONG
def playerBattle(board, playerLeftPieces, computerLeftPieces, x, y, myValue):
    survive = True

    if myValue == "K":  # 왕인경우
        if (x > 0 and (board[x - 1][y].team == "Computer")):  # 정면에서
            if (board[x - 1][y].value == "K"):  # 왕만나면
                board[x][y].visible = True
                board[x - 1][y].visible = True
                print("[Player] : (F)Nothing happen, 왕과 왕이 만났습니다. 서로 오픈합니다.") # 서로 오픈되고 아무일도 안생김

            else:  # 다른것만나면
                board[x - 1][y].visible = True
                survive = False  # 서로 오픈하고 왕죽고 게임 끝
                print("[Player] : (F)Player의 왕이 죽었습니다!")

        elif (y > 0 and board[x][y - 1].team == "Computer"):  # 왼쪽에서
            if (board[x][y - 1].value == "K"):  # 왕만나면
                board[x][y].visible = True
                board[x][y - 1].visible = True
                print("[Player] : (L)Nothing happen, 왕과 왕이 만났습니다. 서로 오픈합니다.") # 서로 오픈되고 아무일도 안생김

            else:  # 다른것만나면
                board[x][y - 1].visible = True
                survive = False  # 서로 오픈하고 왕죽고 게임 끝
                print("[Player] : (L)Player의 왕이 죽었습니다!")

        elif (y < 5 and board[x][y + 1].team == "Computer"):  # 오른쪽에서
            if (board[x][y + 1].value == "K"):  # 왕만나면
                board[x][y].visible = True
                board[x][y + 1].visible = True
                print("[Player] : (R)Nothing happen, 왕과 왕이 만났습니다. 서로 오픈합니다.") # 서로 오픈되고 아무일도 안생김

            else:  # 다른것만나면
                board[x][y + 1].visible = True
                survive = False  # 서로 오픈하고 왕죽고 게임 끝
                print("[Player] : (R)Player의 왕이 죽었습니다!")
    else:
        # front enemy
        if x > 0 and board[x - 1][y].team == "Computer":
            if type(board[x - 1][y].value) == str:
                if board[x - 1][y].value == "K":  # king
                    board[x - 1][y] = chessPieces(True, "S", "none")
                    computerLeftPieces.remove("K")
                    print("[Player] : (F)Catch King, Player가 CPU의 왕을 잡았습니다!")

                elif board[x - 1][y].value == "M":  # mine
                    board[x - 1][y] = chessPieces(True, "S", "none")
                    computerLeftPieces.remove("M")
                    survive = False
                    print("[Player] : (F)Booooooomb, Player가 지뢰를 밟았습니다!")

            else:
                if myValue + board[x - 1][y].value >= 10:
                    print("[Player] : 두 수의 합이 10보다 크거나 같습니다. ", end="")
                    if myValue > board[x - 1][y].value:  # win
                        computerLeftPieces.remove(board[x-1][y].value)
                        print(str(myValue) + " > " + str(board[x - 1][y].value) + " ", end="")
                        board[x - 1][y] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(F)win, Player가 이겼습니다.")

                    elif myValue == board[x - 1][y].value:  # draw (둘 다 죽음)
                        computerLeftPieces.remove(board[x - 1][y].value)
                        print(str(myValue) + " = " + str(board[x - 1][y].value) + " ", end="")
                        board[x - 1][y] = chessPieces(True, "S", "none")
                        survive = False
                        print("(F)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " < " + str(board[x - 1][y].value) + " ", end="")
                        survive = False
                        board[x-1][y].visible = True
                        print("(F)lose, CPU가 이겼습니다.")
                else:
                    print("[Player] : 두 수의 합이 10보다 작습니다. ", end="")
                    if myValue < board[x - 1][y].value:  # win
                        computerLeftPieces.remove(board[x-1][y].value)
                        print(str(myValue) + " < " + str(board[x - 1][y].value) + " ", end="")
                        board[x - 1][y] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(F)win, Player가 이겼습니다.")

                    elif myValue == board[x - 1][y].value:  # draw (둘 다 죽음)
                        print(str(myValue) + " = " + str(board[x - 1][y].value) + " ", end="")
                        computerLeftPieces.remove(board[x-1][y].value)
                        board[x - 1][y] = chessPieces(True, "S", "none")
                        survive = False
                        print("(F)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " > " + str(board[x - 1][y].value) + " ", end="")
                        survive = False
                        board[x - 1][y].visible = True
                        print("(F)lose, CPU가 이겼습니다.")

        # left enemy
        if y > 0 and board[x][y - 1].team == "Computer":
            if type(board[x][y - 1].value) == str:
                if board[x][y - 1].value == "K":  # king
                    board[x][y - 1] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("K")
                    print("[Player] : (L)Catch King, Player가 CPU의 왕을 잡았습니다!")

                elif board[x][y - 1].value == "M":  # mine
                    board[x][y - 1] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("M")
                    survive = False
                    print("[Player] : (L)Booooooomb, Player가 지뢰를 밟았습니다!")

            else:
                # minus rule
                if y == 2 or y == 4:
                    print("[Player] : Minus Rule, 두 수의 합이 10보다 작습니다. ", end="")
                    if myValue < board[x][y - 1].value:  # win
                        print(str(myValue) + " < " + str(board[x][y - 1].value) + " ", end="")
                        computerLeftPieces.remove(board[x][y-1].value)
                        board[x][y - 1] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(L)win, Player가 이겼습니다.")

                    elif myValue == board[x][y - 1].value:  # draw (둘 다 죽음)
                        print(str(myValue) + " = " + str(board[x][y - 1].value) + " ", end="")
                        computerLeftPieces.remove(board[x][y - 1].value)
                        board[x][y - 1] = chessPieces(True, "S", "none")
                        survive = False
                        print("(L)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " > " + str(board[x][y - 1].value) + " ", end="")
                        survive = False
                        board[x][y-1].visible = True
                        print("(L)lose, CPU가 이겼습니다.")

                else: # normal
                    if myValue + board[x][y - 1].value >= 10:
                        print("[Player] : 두 수의 합이 10보다 크거나 같습니다. ", end="")
                        if myValue > board[x][y - 1].value:  # win
                            print(str(myValue) + " > " + str(board[x][y - 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y-1].value)
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(L)win, Player가 이겼습니다.")

                        elif myValue == board[x][y - 1].value:  # draw (둘 다 죽음)
                            print(str(myValue) + " = " + str(board[x][y - 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y - 1].value)
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(L)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " < " + str(board[x][y - 1].value) + " ", end="")
                            survive = False
                            board[x][y - 1].visible = True
                            print("(L)lose, CPU가 이겼습니다.")
                    else:
                        print("[Player] : 두 수의 합이 10보다 작습니다. ", end="")
                        if myValue < board[x][y - 1].value:  # win
                            print(str(myValue) + " < " + str(board[x][y - 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y - 1].value)
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(L)win, Player가 이겼습니다.")

                        elif myValue == board[x][y - 1].value:  # draw (둘 다 죽음)
                            print(str(myValue) + " = " + str(board[x][y - 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y - 1].value)
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(L)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " > " + str(board[x][y - 1].value) + " ", end="")
                            survive = False
                            board[x][y - 1].visible = True
                            print("(L)lose, CPU가 이겼습니다.")

        # right enemy
        if y < 5 and board[x][y + 1].team == "Computer":
            if type(board[x][y + 1].value) == str:
                if board[x][y + 1].value == "K":  # king
                    board[x][y + 1] = chessPieces(True, "S", "none")
                    computerLeftPieces.remove("K")
                    print("[Player] : (R)Catch King, Player가 CPU의 왕을 잡았습니다!")

                elif board[x][y + 1].value == "M":  # mine
                    board[x][y + 1] = chessPieces(True, "S", "none")
                    computerLeftPieces.remove("M")
                    survive = False
                    print("[Player] : (R)Booooooomb, Player가 지뢰를 밟았습니다!")

            else:
                # minus rule
                if y == 1 or y == 3:
                    print("[Player] : Minus Rule, 두 수의 합이 10보다 작습니다. ", end="")
                    if myValue < board[x][y + 1].value:  # win
                        print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                        computerLeftPieces.remove(board[x][y + 1].value)
                        board[x][y + 1] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(R)win, Player가 이겼습니다.")

                    elif myValue == board[x][y + 1].value:  # draw (둘 다 죽음)
                        print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                        computerLeftPieces.remove(board[x][y + 1].value)
                        board[x][y + 1] = chessPieces(True, "S", "none")
                        survive = False
                        print("(R)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                        survive = False
                        board[x][y + 1].visible = True
                        print("(R)lose, CPU가 이겼습니다.")

                else:
                    if myValue + board[x][y + 1].value >= 10:
                        print("[Player] : 두 수의 합이 10보다 크거나 같습니다. ", end="")
                        if myValue > board[x][y + 1].value:  # win
                            print(str(myValue) + " > " + str(board[x][y + 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y + 1].value)
                            board[x][y + 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(R)win, Player가 이겼습니다.")

                        elif myValue == board[x][y + 1].value:  # draw (둘 다 죽음)
                            print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y + 1].value)
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(R)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                            survive = False
                            board[x][y + 1].visible = True
                            print("(R)lose, CPU가 이겼습니다.")
                    else:
                        print("[CPU] : 두 수의 합이 10보다 작습니다. ", end="")
                        if myValue < board[x][y + 1].value:  # win
                            print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y + 1].value)
                            board[x][y + 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(R)win, Player가 이겼습니다.")

                        elif myValue == board[x][y + 1].value:  # draw (둘 다 죽음)
                            print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                            computerLeftPieces.remove(board[x][y + 1].value)
                            board[x][y + 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(R)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " > " + str(board[x][y + 1].value) + " ", end="")
                            survive = False
                            board[x][y + 1].visible = True
                            print("(R)lose, Player가 이겼습니다.")

    if not survive:  # set my value
        playerLeftPieces.remove(myValue)
        board[x][y] = chessPieces(True, "S", "none")

    return board, playerLeftPieces, computerLeftPieces

def computerPart(board, playerLeftPieces, computerLeftPieces):  # BEAK

    systemMsg = "[SYSTEM] : CPU가 "
    l = [1, 4, 5, 6, 3, 8];
    x = 100;
    y = 100
    while True:
        marker = random.choice(computerLeftPieces)  # 움직일 말 고르기
        while (marker == "M"):
            marker = random.choice(computerLeftPieces)  # 지뢰이면 다시 선택

        for i in range(9):
            for j in range(6):
                if (board[i][j].team == "Computer") and (marker == board[i][j].value):  # 움직일 말의 좌표 찾기
                    x = i
                    y = j

        random.shuffle(l)  # 움직일 방향 정하기
        direction = l[0]

        if (direction == 1 and y - 1 >= 0 and board[x][y - 1].value == "S"):  # 왼쪽으로 움직이기
            board[x][y - 1] = board[x][y]
            board[x][y] = chessPieces(True, "S", "none")
            systemMsg += "(" + str(x) + "," + str(y) + ")에 있는 말을 "
            x = x
            y = y - 1  # 베틀시 필요한 주소 저장
            break

        elif (direction == 3 and y + 1 < 6 and board[x][y + 1].value == "S"):  # 오른쪽으로 움직이기
            board[x][y + 1] = board[x][y]
            board[x][y] = chessPieces(True, "S", "none")
            systemMsg += "(" + str(x) + "," + str(y) + ")에 있는 말을 "
            x = x
            y = y + 1  # 베틀시 필요한 주소 저장
            break

        elif (direction == 5 and x + 1 < 9 and board[x + 1][y].value == "S"):  # 앞으로(아래로) 움직이기
            board[x + 1][y] = board[x][y]
            board[x][y] = chessPieces(True, "S", "none")
            systemMsg += "(" + str(x) + "," + str(y) + ")에 있는 말을 "
            x = x + 1
            y = y  # 베틀시 필요한 주소 저장
            break

        elif (direction == 8 and x + 2 < 9 and board[x + 1][y].value == "S" and board[x + 2][
            y].value == "S"):  # 앞으로(아래로) 2칸 움직이기
            board[x + 2][y] = board[x][y]
            board[x][y] = chessPieces(True, "S", "none")
            systemMsg += "(" + str(x) + "," + str(y) + ")에 있는 말을 "
            x = x + 2
            y = y  # 베틀시 필요한 주소 저장
            break

        elif (direction == 4 and y - 1 >= 0 and x + 1 < 9 and board[x + 1][y - 1].value == "S"):  # 왼쪽 아래 대각선으로 움직이기
            board[x + 1][y - 1] = board[x][y]
            board[x][y] = chessPieces(True, "S", "none")
            systemMsg += "(" + str(x) + "," + str(y) + ")에 있는 말을 "
            x = x + 1
            y = y - 1  # 베틀시 필요한 주소 저장
            break

        elif (direction == 6 and y + 1 < 6 and x + 1 < 9 and board[x + 1][y + 1].value == "S"):  # 오른쪽 아래 대각선으로 움직이기
            board[x + 1][y + 1] = board[x][y]
            board[x][y] = chessPieces(True, "S", "none")
            systemMsg += "(" + str(x) + "," + str(y) + ")에 있는 말을 "
            x = x + 1
            y = y + 1  # 베틀시 필요한 주소 저장
            break

        else:
            continue  # 갖혀있는 말이나, 움직일 방향이 없으면 다시 선택

    systemMsg += "(" + str(x) + "," + str(y) + ")로 움직였습니다."
    print(systemMsg)

    board, playerLeftPieces, computerLeftPieces = computerBattle(board, playerLeftPieces, computerLeftPieces, x, y, board[x][y].value)

    # revive
    # INYEONG BAEK
    if (x - 1 == 7 and (direction == 4 or direction == 5 or direction == 6)) or (
            x - 2 == 7 and (direction == 8)):  # reach end
        rescuablePieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in computerLeftPieces:  # set possible pieces
            if type(i) == int:
                rescuablePieces.remove(i)
        if rescuablePieces == []:
            print("[SYSTEM] : 부활에 실패했습니다. 살릴 수 있는 말이 없습니다.")
        else:
            possibleIndex = [0, 1, 2, 3, 4, 5]
            for i in range(6):
                if board[0][i].value != "S":  # COM 0번줄의 공백여부 판단
                    possibleIndex.remove(i)
            if possibleIndex == []:
                print("[SYSTEM] : 부활에 실패했습니다. CPU의 첫 번째 줄이 가득찼습니다.")
            else:
                random.shuffle(rescuablePieces);
                random.shuffle(possibleIndex)
                print("[SYSTME] : 영웅은 죽지 않아요! (0, " + str(possibleIndex[0]) + ")에 " + str(
                    rescuablePieces[0]) + "이/가 부활했습니다!")
                board[0][possibleIndex[0]] = chessPieces(True, rescuablePieces[0], "Computer")
                computerLeftPieces.append(rescuablePieces[0])

    return board, playerLeftPieces, computerLeftPieces

# INYEONG
def computerBattle(board, playerLeftPieces, computerLeftPieces, x, y, myValue):
    survive = True

    if myValue == "K":  # 왕인경우
        if (x < 8 and (board[x + 1][y].team == "Player")):  # 정면에서
            if (board[x + 1][y].value == "K"):  # 왕만나면
                board[x][y].visible = True
                board[x + 1][y].visible = True
                print("[SYSTEM] : (F)Nothing happen, 왕과 왕이 만났습니다. 서로 오픈합니다.")  # 서로 오픈되고 아무일도 안생김

            else:  # 다른것만나면
                board[x + 1][y].visible = True
                survive = False  # 서로 오픈하고 왕죽고 게임 끝
                print("[SYSTEM] : (F)CPU의 왕이 죽었습니다!")

        elif (y > 0 and board[x][y - 1].team == "Player"):  # 왼쪽에서
            if (board[x][y - 1].value == "K"):  # 왕만나면
                board[x][y].visible = True
                board[x][y - 1].visible = True
                print("[SYSTEM] : (L)Nothing happen, 왕과 왕이 만났습니다. 서로 오픈합니다.")  # 서로 오픈되고 아무일도 안생김

            else:  # 다른것만나면
                board[x][y - 1].visible = True
                survive = False  # 서로 오픈하고 왕죽고 게임 끝
                print("[SYSTEM] : (L)CPU의 왕이 죽었습니다!")

        elif (y < 5 and board[x][y + 1].team == "Player"):  # 오른쪽에서
            if (board[x][y + 1].value == "K"):  # 왕만나면
                board[x][y].visible = True
                board[x][y + 1].visible = True
                print("[SYSTEM] : (R)Nothing happen, 왕과 왕이 만났습니다. 서로 오픈합니다.")  # 서로 오픈되고 아무일도 안생김

            else:  # 다른것만나면
                board[x][y + 1].visible = True
                survive = False  # 서로 오픈하고 왕죽고 게임 끝
                print("[SYSTEM] : (R)CPU의 왕이 죽었습니다!")
    else:
        # front enemy
        if x < 8 and board[x + 1][y].team == "Player":
            if type(board[x + 1][y].value) == str:
                if board[x + 1][y].value == "K":  # king
                    board[x + 1][y] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("K")
                    print("[SYSTEM] : (F)Catch King, CPU가 Player의 왕을 잡았습니다!")

                elif board[x + 1][y].value == "M":  # mine
                    board[x + 1][y] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("M")
                    survive = False
                    print("[SYSTEM] : (F)Booooooomb, CPU가 지뢰를 밟았습니다!")

            else:
                if myValue + board[x + 1][y].value >= 10:
                    print("[SYSTEM] : 두 수의 합이 10보다 크거나 같습니다. ", end="")
                    if myValue > board[x + 1][y].value:  # win
                        playerLeftPieces.remove(board[x + 1][y].value)
                        print(str(myValue) + " > " + str(board[x + 1][y].value) + " ", end="")
                        board[x + 1][y] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(F)win, CPU가 이겼습니다.")

                    elif myValue == board[x + 1][y].value:  # draw (둘 다 죽음)
                        playerLeftPieces.remove(board[x + 1][y].value)
                        print(str(myValue) + " = " + str(board[x + 1][y].value) + " ", end="")
                        board[x + 1][y] = chessPieces(True, "S", "none")
                        survive = False
                        print("(F)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " < " + str(board[x + 1][y].value) + " ", end="")
                        survive = False
                        print("(F)lose, Player가 이겼습니다.")
                else:
                    print("[SYSTEM] : 두 수의 합이 10보다 작습니다. ", end="")
                    if myValue < board[x + 1][y].value:  # win
                        playerLeftPieces.remove(board[x + 1][y].value)
                        print(str(myValue) + " < " + str(board[x + 1][y].value) + " ", end="")
                        board[x + 1][y] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(F)win, CPU가 이겼습니다.")

                    elif myValue == board[x + 1][y].value:  # draw (둘 다 죽음)
                        playerLeftPieces.remove(board[x + 1][y].value)
                        print(str(myValue) + " = " + str(board[x + 1][y].value) + " ", end="")
                        board[x + 1][y] = chessPieces(True, "S", "none")
                        survive = False
                        print("(F)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " > " + str(board[x + 1][y].value) + " ", end="")
                        survive = False
                        print("(F)lose, Player가 이겼습니다.")

        # left enemy
        if y > 0 and board[x][y - 1].team == "Player":
            if type(board[x][y - 1].value) == str:
                if board[x][y - 1].value == "K":  # king
                    board[x][y - 1] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("K")
                    print("[SYSTEM] : (L)Catch King, CPU가 Player의 왕을 잡았습니다!")

                elif board[x][y - 1].value == "M":  # mine
                    board[x][y - 1] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("M")
                    survive = False
                    print("[SYSTEM] : (L)Booooooomb, CPU가 지뢰를 밟았습니다!")

            else:
                # minus rule
                if y == 2 or y == 4:
                    print("[SYSTEM] : Minus Rule, 두 수의 합이 10보다 작습니다. ", end="")
                    if myValue < board[x][y - 1].value:  # win
                        playerLeftPieces.remove(board[x][y - 1].value)
                        print(str(myValue) + " < " + str(board[x][y - 1].value) + " ", end="")
                        board[x][y - 1] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(L)win, CPU가 이겼습니다.")

                    elif myValue == board[x][y - 1].value:  # draw (둘 다 죽음)
                        playerLeftPieces.remove(board[x][y - 1].value)
                        print(str(myValue) + " = " + str(board[x][y - 1].value) + " ", end="")
                        board[x][y - 1] = chessPieces(True, "S", "none")
                        survive = False
                        print("(L)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " > " + str(board[x][y - 1].value) + " ", end="")
                        survive = False
                        print("(L)lose, Player가 이겼습니다.")

                else:
                    if myValue + board[x][y - 1].value >= 10:
                        print("[SYSTEM] : 두 수의 합이 10보다 크거나 같습니다. ", end="")
                        if myValue > board[x][y - 1].value:  # win
                            playerLeftPieces.remove(board[x][y - 1].value)
                            print(str(myValue) + " > " + str(board[x][y - 1].value) + " ", end="")
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(L)win, CPU가 이겼습니다.")

                        elif myValue == board[x][y - 1].value:  # draw (둘 다 죽음)
                            playerLeftPieces.remove(board[x][y - 1].value)
                            print(str(myValue) + " = " + str(board[x][y - 1].value) + " ", end="")
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(L)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " < " + str(board[x][y - 1].value) + " ", end="")
                            survive = False
                            print("(L)lose, Player가 이겼습니다.")
                    else:
                        print("[SYSTEM] : 두 수의 합이 10보다 작습니다. ", end="")
                        if myValue < board[x][y - 1].value:  # win
                            playerLeftPieces.remove(board[x][y - 1].value)
                            print(str(myValue) + " < " + str(board[x][y - 1].value) + " ", end="")
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(L)win, CPU가 이겼습니다.")

                        elif myValue == board[x][y - 1].value:  # draw (둘 다 죽음)
                            playerLeftPieces.remove(board[x][y - 1].value)
                            print(str(myValue) + " = " + str(board[x][y - 1].value) + " ", end="")
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(L)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " > " + str(board[x][y - 1].value) + " ", end="")
                            survive = False
                            print("(L)lose, Player가 이겼습니다.")

        # right enemy
        if y < 5 and board[x][y + 1].team == "Player":
            if type(board[x][y + 1].value) == str:
                if board[x][y + 1].value == "K":  # king
                    board[x][y + 1] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("K")
                    print("[SYSTEM] : (R)Catch King, CPU가 Player의 왕을 잡았습니다!")

                elif board[x][y + 1].value == "M":  # mine
                    board[x][y + 1] = chessPieces(True, "S", "none")
                    playerLeftPieces.remove("M")
                    survive = False
                    print("[SYSTEM] : (R)Booooooomb, CPU가 지뢰를 밟았습니다!")

            else:
                # minus rule
                if y == 1 or y == 3:
                    print("[SYSTEM] : Minus Rule, 두 수의 합이 10보다 작습니다. ", end="")
                    if myValue < board[x][y + 1].value:  # win
                        playerLeftPieces.remove(board[x][y + 1].value)
                        print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                        board[x][y + 1] = chessPieces(True, "S", "none")
                        board[x][y].visible = True  # set visible
                        print("(R)win, CPU가 이겼습니다.")

                    elif myValue == board[x][y + 1].value:  # draw (둘 다 죽음)
                        playerLeftPieces.remove(board[x][y + 1].value)
                        print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                        board[x][y + 1] = chessPieces(True, "S", "none")
                        survive = False
                        print("(R)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                    else:  # lose
                        print(str(myValue) + " > " + str(board[x][y + 1].value) + " ", end="")
                        survive = False
                        print("(R)lose, Player가 이겼습니다.")

                else:
                    if myValue + board[x][y + 1].value >= 10:
                        print("[SYSTEM] : 두 수의 합이 10보다 크거나 같습니다. ", end="")
                        if myValue > board[x][y + 1].value:  # win
                            playerLeftPieces.remove(board[x][y + 1].value)
                            print(str(myValue) + " > " + str(board[x][y + 1].value) + " ", end="")
                            board[x][y + 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(R)win, CPU가 이겼습니다.")

                        elif myValue == board[x][y + 1].value:  # draw (둘 다 죽음)
                            playerLeftPieces.remove(board[x][y + 1].value)
                            print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                            board[x][y - 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(R)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                            survive = False
                            print("(R)lose, Player가 이겼습니다.")
                    else:
                        print("[SYSTEM] : 두 수의 합이 10보다 작습니다. ", end="")
                        if myValue < board[x][y + 1].value:  # win
                            playerLeftPieces.remove(board[x][y + 1].value)
                            print(str(myValue) + " < " + str(board[x][y + 1].value) + " ", end="")
                            board[x][y + 1] = chessPieces(True, "S", "none")
                            board[x][y].visible = True  # set visible
                            print("(R)win, CPU가 이겼습니다.")

                        elif myValue == board[x][y + 1].value:  # draw (둘 다 죽음)
                            playerLeftPieces.remove(board[x][y + 1].value)
                            print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                            board[x][y + 1] = chessPieces(True, "S", "none")
                            survive = False
                            print("(R)draw, 비겼습니다. 두 말 모두 제거 됩니다.")

                        else:  # lose
                            print(str(myValue) + " = " + str(board[x][y + 1].value) + " ", end="")
                            survive = False
                            print("(R)lose, Player가 이겼습니다.")

    if not survive:  # set my value
        computerLeftPieces.remove(myValue)
        board[x][y] = chessPieces(True, "S", "none")

    return board, playerLeftPieces, computerLeftPieces


def numberKoreanChess():

    print("\n************** 숫자 장기 승리조건 **************")
    print(" 1. 상대편 왕을 잡은경우")
    print(" 2. 상대편 왕빼고 모든 말을 잡은경우(지뢰포함)")
    print(" 3. 왕이 상대편 진영끝에 도달한 경우")
    # print(" 4. 60초이내 안움직인 경우")  # playerPart 내부에서 처리
    print("\n Game referrence : 더 지니어스(그랜드 파이널)")
    print("*********************************************\n")

    board = initBoard()  # main board
    playerLeftPieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "M", "M", "M"]
    computerLeftPieces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "M", "M", "M"]
    s = ""
    startFirst = True

    while not (s == "Y" or s == "y" or s == "N" or s == "n"):
        s = input("먼저 시작하시겠습니까?(y/n) : ")

    if s == "n" or s == "N":
        startFirst = False

    printBorad(board, playerLeftPieces, computerLeftPieces)

    while True:
        if startFirst:
            board, playerLeftPieces, computerLeftPieces = playerPart(board, playerLeftPieces, computerLeftPieces)

            # check list condition (종료조건 1, 2)
            stat, winner = checkEndListCondition(playerLeftPieces, computerLeftPieces)
            if not stat:
                # check board condition (종료조건 3)
                stat, winner = checkEndBoardCondition(board)

            if stat: break

            board, playerLeftPieces, computerLeftPieces = computerPart(board, playerLeftPieces, computerLeftPieces)
            stat, winner = checkEndListCondition(playerLeftPieces, computerLeftPieces)
            if not stat:
                stat, winner = checkEndBoardCondition(board)

            if stat: break

        else:
            board, playerLeftPieces, computerLeftPieces = computerPart(board, playerLeftPieces, computerLeftPieces)
            stat, winner = checkEndListCondition(playerLeftPieces, computerLeftPieces)
            if not stat:
                stat, winner = checkEndBoardCondition(board)

            if stat: break

            board, playerLeftPieces, computerLeftPieces = playerPart(board, playerLeftPieces, computerLeftPieces)
            stat, winner = checkEndListCondition(playerLeftPieces, computerLeftPieces)
            if not stat:
                stat, winner = checkEndBoardCondition(board)

            if stat: break

        print()

        printBorad(board, playerLeftPieces, computerLeftPieces)

        # # check list condition (종료조건 1, 2)
        # stat, winner = checkEndListCondition(playerLeftPieces, computerLeftPieces)
        # if not stat:
        #     # check board condition (종료조건 3)
        #     stat, winner = checkEndBoardCondition(board)
        #
        # if stat: break

    # game over show all pieces
    for i in range(9):
        for j in range(6):
            board[i][j].visible = True

    printBorad(board, playerLeftPieces, computerLeftPieces)
    print(C_BOLD + C_YELLOW + "\n[SYSTEM] : Winner is " + winner + C_END)
    print(C_BOLD + C_CYAN + "\n\nMade by Team 없음(9조, 백승헌, 하민수, 김인영)" + C_END)


numberKoreanChess()