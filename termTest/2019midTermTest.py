# 제출시 파일 이름 형식은 2019000000-도선생.py
# 반 : 1시
# 학번 : 2016015878
# 이름 : 김인영
# 구글클래스 이름 : INYEONG KIM

## 2. 2차방정식 근의 공식 (end)

import math

def quadraticEquationPositive(a, b, c):
    if a != 0:
        if pow(b,2)-4*a*c <= 0:
            return None
        else:
            return (((-b+math.sqrt(b**2-4*a*c))/(2*a)), ((-b-math.sqrt(b**2-4*a*c))/(2*a)))
    else:
        return None

# print(quadraticEquationPositive(1,-1,-2)) # (2.0, -1.0)
# print(quadraticEquationPositive(3,3,3)) # None
# print(quadraticEquationPositive(0,3,4)) # None

### 3. 24시간 시계 형식 확인 (end)

def validClock24(time):
    (hour, colon, minute) = time.partition(":")
    if len(hour)!=2 or len(minute)!=2:
        return False
    hour = int(hour)
    minute = int(minute)

    if hour > 24:
        return False
    elif hour==24:
        return minute==0
    else:
        return minute<=59

# print(validClock24("00:00")) # True
# print(validClock24("00:30")) # True
# print(validClock24("09:58")) # True
# print(validClock24("12:15")) # True
# print(validClock24("23:59")) # True
# print(validClock24("24:00")) # True
# print(validClock24("7:07")) # False
# print(validClock24("07:121")) # False
# print(validClock24("13:4")) # False
# print(validClock24("00:60")) # False
# print(validClock24("24:01")) # False
# print(validClock24("25:10")) # False


### 4. 24시간 시계를 12시간 시계로 변환 (end)

def clock24to12(time):
    (hour, colon, minute) = time.partition(":")
    hour = int(hour)
    minute = int(minute)

    res = ""
    if hour >= 12:
        if hour - 12 == 0:
            res += str(hour) + ":"
        else:
            res += str(hour-12) + ":"

        if minute < 10:
            res += "0" + str(minute)
        else:
            res += str(minute)

        if hour == 24:
            res += "am"
        else:
            res += "pm"
    else:
        if hour == 0:
            res += "12" + ":"
        else:
            res += str(hour) + ":"

        if minute < 10:
            res += "0" + str(minute) + "am"
        else:
            res += str(minute) + "am"

    return res

# print(clock24to12("00:00")) # "12:00am"
# print(clock24to12("00:05")) # "12:05am"
# print(clock24to12("09:58")) # "9:58am"
# print(clock24to12("11:43")) # "11:43am"
# print(clock24to12("12:08")) # "12:08pm"
# print(clock24to12("15:50")) # "3:50pm"
# print(clock24to12("20:20")) # "8:20pm"
# print(clock24to12("24:00")) # "12:00am"


### 5. 소요시간 계산하기 (end)

def timePassed(fromTime, toTime):
    (hour1, _, minute1) = fromTime.partition(":")
    (hour2, _, minute2) = toTime.partition(":")

    minute1 = int(minute1)
    minute1 += 60*int(hour1)

    minute2 = int(minute2)
    minute2 += 60 * int(hour2)

    minute = minute2-minute1
    return str(minute//60) + ":" + str(minute%60)


# print(timePassed("03:12", "03:25"))  # "0:13"
# print(timePassed("11:45", "13:15"))  # "1:30"
# print(timePassed("06:15", "07:45"))  # "1:30"
# print(timePassed("03:34", "05:00"))  # "1:26"


### 6. 일반재귀 함수를 꼬리재귀 함수로 변환하기 (end)
def adjust(ns):
    if len(ns) > 1:
        if ns[0] < ns[1]:
            return [ns[0] + 1] + adjust(ns[1:])
        elif ns[0] > ns[1]:
            return [ns[0] - 1] + adjust(ns[1:])
        else:
            return [ns[0]] + adjust(ns[1:])
    else:
        return ns


# print(adjust([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjust([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjust([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjust([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjust([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def adjustT(ns):
    def loop(ns, rs):
        if len(ns) > 1:
            if ns[0] < ns[1]:
                return loop(ns[1:], rs + [ns[0]+1])
            elif ns[0] > ns[1]:
                return loop(ns[1:], rs + [ns[0] - 1])
            else:
                return loop(ns[1:], rs + [ns[0]])
        else:
            return rs + ns

    return loop(ns, [])


# print(adjustT([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjustT([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjustT([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustT([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustT([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

### 7. 꼬리재귀 함수를 while 루프 함수로 변환하기 (end)
def adjustW(ns):
    l = len(ns)
    start = ns[0]
    i = 0
    while i < l:
        if start < ns[i]:
            ns[i-1] += 1
        elif start > ns[i]:
            ns[i - 1] -= 1
        start = ns[i]
        i += 1
    return ns

# print(adjustW([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjustW([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjustW([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustW([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustW([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

### 8. for 루프 함수로 만들기 (end)
def adjustF(ns):
    l = len(ns)
    start = ns[0]
    for i in range(1,l):
        if start < ns[i]:
            ns[i-1] += 1
        if start > ns[i]:
            ns[i-1] -= 1
        start = ns[i]
    return ns

# print(adjustF([4, 6, 5, 3, 7, 6, 2, 1, 3, 2]))
#              # [5, 5, 4, 4, 6, 5, 1, 2, 2, 2]
# print(adjustF([5, 4, 4, 5, 5, 4, 2, 2, 2, 2]))
#              # [4, 4, 5, 5, 4, 3, 2, 2, 2, 2]
# print(adjustF([4, 3, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustF([3, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(adjustF([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
#              # [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]


### 9. 리스트의 원소가 모두 같은지 확인 (end)

def allequal(ns):
    if len(ns) > 1:
        x = ns[0]
        for i in range(len(ns)):
            if x != ns[i]:
                return False
        return True
    else:
        return True

# print(allequal([4, 6, 5, 3, 7, 6, 2, 1, 3, 2])) # False
# print(allequal([5, 5, 4, 4, 6, 5, 1, 2, 2, 2])) # False
# print(allequal([3, 2, 2, 2, 2, 2, 2, 2, 2, 2])) # False
# print(allequal([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])) # True
# print(allequal([2])) # True
# print(allequal([])) # True

### 10. 동일화 노력 (end)

def equalizer(ns):
    def allequal(ns):
        if len(ns) > 1:
            x = ns[0]
            for i in range(len(ns)):
                if x != ns[i]:
                    return False
            return True
        else:
            return True

    def adjust(ns):
        if len(ns) > 1:
            if ns[0] < ns[1]:
                return [ns[0] + 1] + adjust(ns[1:])
            elif ns[0] > ns[1]:
                return [ns[0] - 1] + adjust(ns[1:])
            else:
                return [ns[0]] + adjust(ns[1:])
        else:
            return ns

    count = 0
    while not allequal(ns):
        ns = adjust(ns)
        count+=1
    return count


# print(equalizer([4, 6, 5, 3, 7, 6, 2, 1, 3, 2])) # 9
# print(equalizer([8, 2, 5, 7, 1, 1, 6, 7, 4, 8])) # 12
# print(equalizer([8, 4, 5, 6, 9, 8, 6, 2, 0, 6])) # 14
# print(equalizer([4, 0, 1, 0, 3, 4, 3, 3, 7, 9])) # 13
# print(equalizer([1, 6, 5, 6, 8, 5, 3, 3, 3, 8])) # 13
# print(equalizer([])) # 0
# print(equalizer([5])) # 0
# print(equalizer([4, 4, 4])) # 0
# print(equalizer([4, 3])) # 1
# print(equalizer([4, 5])) # 1
# print(equalizer([4, 5, 4])) # 2
# print(equalizer([14, 69, 87, 13, 0, 16, 83, 19, 45, 88])) # 92


### 11. 아나그램 확인 (sort() 함수 사용 금지) (end)

def isanagram(word1, word2):
    while word1 != '':
        if word1[0] in word2:
            idx = word2.find(word1[0])
            word1 = word1[1:]

            twolen = len(word2)
            word2 = (word2[0:idx] + word2[idx+1:twolen])

        else:
            return False
    return word2 == ''

# print(isanagram('silent', 'listen'))
# print(isanagram('elvis', 'lives'))
# print(isanagram('restful', 'fluster'))
# print(isanagram('문전박대', '대박전문'))

### 12. 이진수 덧셈 - 자리수는 같다고 가정 (end)
### 숫자열은 '0' 또는 '1'로만 구성된다.

def addBinary(n1, n2):
    answer = ''
    l = len(n1)
    c = 0
    for i in range(l-1, -1, -1):
        x = int(n1[i]) + int(n2[i]) + c
        if x==0:
            c = 0
            answer += "0"
        elif x==1:
            c = 0
            answer += "1"
        elif x==2:
            c = 1
            answer += "0"
        elif x==3:
            c = 1
            answer += "1"
    if c==1:
        answer += "1"
    return answer[::-1]

# print(addBinary('','')) # ''
# print(addBinary('0','0')) # '0'
# print(addBinary('1','0')) # '1'
# print(addBinary('0','1')) # '1'
# print(addBinary('1','1')) # '10'
# print(addBinary('10','11')) # '101'
# print(addBinary('11','11')) # '110'
# print(addBinary('1011','1101')) # '11000'
# print(addBinary('1111','1111')) # '11110'
# print(addBinary('11011001','00011011')) # '11110100'