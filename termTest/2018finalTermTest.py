# 1. 정방행렬 검사(대칭여부 파악)
def symmetric(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(size):
            if sqmat[i][j] != sqmat[j][i]:
                return False
    return True
# print(symmetric([[2,3],[3,2]])) # True
# print(symmetric([[2,3],[2,3]])) # False
# print(symmetric([[1,7,3],[7,4,-5],[3,-5,6]])) # True
# print(symmetric([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])) # True
# print(symmetric([[1,2,3,4],[2,1,4,3],[3,4,1,2],[4,3,2,1]])) # True

# 2. 시간더하기
def addtime(time1,time2):
    h1 = int(time1[0])
    m1 = int(time1[1:3])
    s1 = int(time1[3:5])
    s1 += (60 * m1 + 3600 * h1)

    h = int(time2[0])
    m = int(time2[1:3])
    s = int(time2[3:5])
    s += (60*m + 3600*h + s1)

    res=str(s//3600)
    if (s%3600)//60 < 10:
        res+="0"
    res+=str((s%3600)//60)
    if (s%3600)%60 < 10:
        res+="0"
    res+=str((s%3600)%60)
    return res
# print(addtime("01457","02502")) # "03959"
# print(addtime("01457","05101")) # "10558"
# print(addtime("01457","05118")) # "10615"
# print(addtime("94357","85145")) # "183542"

# 3. 가장 빈번하게 나타나는 숫자
def themost(s):
    if s == "":
        return ""
    else:
        frequency = [0,0,0,0,0,0,0,0,0,0]
        for i in range(len(s)):
            frequency[int(s[i])]+=1
        res=""
        for i in range(len(frequency)):
            if max(frequency) == frequency[i]:
                res+= str(i)

        return res

# print(themost("")) # ""
# print(themost("1")) # "1"
# print(themost("1223334444555")) # "4"
# print(themost("13344")) # "34"
# print(themost("1234")) # "1234"
# print(themost("92039483739203483992019847")) # "9"
# print(themost("00000000000")) # "0"

# 4. 빈자리 채워넣기
def fillthegap(ms):
    def loop(ms,ns):
        if ms != []:
            last = ns[len(ns)-1]
            nxt = ms[0]

            if last > nxt:
                for i in range(last-1, nxt-1, -1):
                    ns.append(i)
            elif last < nxt:
                for i in range(last+1, nxt+1):
                    ns.append(i)
            else:
                ns.append(nxt)

            return loop(ms[1:],ns)
        else:
            return ns
    if ms != []:
        return loop(ms[1:],[ms[0]])
    else:
        return []

# def fillthegap(ms):
#     if ms==[]:
#         return []
#     if len(ms)==1:
#         return ms
#     res = []
#     start = ms[0]
#
#     for i in range(1,len(ms)):
#         if start > ms[i]:
#             for j in range(start, ms[i], -1):
#                 res.append(j)
#         elif start < ms[i]:
#             for j in range(start, ms[i]):
#                 res.append(j)
#         else:
#             res.append(ms[i])
#         start = ms[i]
#
#     res.append(ms[len(ms)-1])
#     return res

# print(fillthegap([])) # []
# print(fillthegap([3])) # [3]
# print(fillthegap([3,3,3])) # [3,3,3]
# print(fillthegap([3,2])) # [3,2]
# print(fillthegap([3,5])) # [3,4,5]
# print(fillthegap([3,6,6,2])) # [3,4,5,6,6,5,4,3,2]
# print(fillthegap([9,2,5,4])) # [9,8,7,6,5,4,3,2,3,4,5,4]

# 5. 16진수 10진수 변환
def hex2dec(hex):
    length = len(hex)
    dec = 0
    for i in range(length):
        h = hex[i]
        if '0' <= h <= '9':
            dec += int(h)*int(pow(16, length-i-1))
        else:
            dec += int(ord(h)-ord('A')+10)*int(pow(16, length-i-1))
    return dec

# print(hex2dec("9C4")) # 2500
# print(hex2dec('5B')) # 91
# print(hex2dec('100')) # 256
# print(hex2dec('ACE')) # 2766
# print(hex2dec('DAD')) # 3501
# print(hex2dec('F0F')) # 3855
# print(hex2dec('1024')) # 4132
# print(hex2dec('CC55')) # 52309

# 6. 10진수 16진수 변환 (문자열 뒤집기)
def dec2hex(dec):
    hex = ''
    while not (dec == 0):
        r = dec % 16
        if r<10:
            hex+=str(r)
        else:
            r-=10
            hex+=chr(ord('A')+r)
        dec = dec // 16
    return hex[::-1]

# print(dec2hex(2500)) # '9C4'
# print(dec2hex(91)) # '5B'
# print(dec2hex(256)) # '100'
# print(dec2hex(2766)) # 'ACE'
# print(dec2hex(3501)) # 'DAD'
# print(dec2hex(3855)) # 'F0F'
# print(dec2hex(4132)) # '1024'
# print(dec2hex(52309)) # 'CC55'

# 7. 퍼트리기
def spread(board):
    n = len(board)
    clone = []

    for i in range(n):
        row = board[i][:]
        clone.append(row)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                if i<n-1:
                    clone[i+1][j] = 1
                if i>0:
                    clone[i-1][j] = 1
                if j < n - 1:
                    clone[i][j+1] = 1
                if j > 0:
                    clone[i][j-1] = 1
    return clone

def print_square(board):
    length = len(board)
    for i in range(length):
        for j in range(length):
            print(board[i][j],end=' ')
        print()
    print()
# board1 = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,1,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]
# print_square(board1)
# board2 = spread(board1)
# print_square(board2)
# board3 = spread(board2)
# print_square(board3)
# board4 = spread(board3)
# print_square(board4)
# board5 = spread(board4)
# print_square(board5)

# board1 = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,1,0],
#          [0,0,0,0,0]]
# print_square(board1)
# board2 = spread(board1)
# print_square(board2)
# board3 = spread(board2)
# print_square(board3)
# board4 = spread(board3)
# print_square(board4)
# board5 = spread(board4)
# print_square(board5)

# board1 = [[1,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]
# print_square(board1)
# board2 = spread(board1)
# print_square(board2)
# board3 = spread(board2)
# print_square(board3)
# board4 = spread(board3)
# print_square(board4)
# board5 = spread(board4)
# print_square(board5)