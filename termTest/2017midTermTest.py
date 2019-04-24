# 1. 삼각수(재귀함수)
def trinum(n):
    if n >= 1:
        return trinum(n-1) + n
    else:
        return 0

# print(trinum(1)) # 1
# print(trinum(3)) # 6
# print(trinum(6)) # 21
# print(trinum(11)) # 66
# print(trinum(0)) # 0
# print(trinum(-3)) # 0

# 삼각수(꼬리재귀함수)
def trinumT(n):
    def loop(n,r):
        if n>0:
            return loop(n-1, r+n)
        else:
            return r
    return loop(n, 0)

# print(trinumT(1)) # 1
# print(trinumT(3)) # 6
# print(trinumT(6)) # 21
# print(trinumT(11)) # 66
# print(trinumT(0)) # 0
# print(trinumT(-3)) # 0

# 삼각수(while 문 함수)
def trinumW(n):
    res = 0
    while n>0:
        res += n
        n-=1
    return res

# print(trinumW(1)) # 1
# print(trinumW(3)) # 6
# print(trinumW(6)) # 21
# print(trinumW(11)) # 66
# print(trinumW(0)) # 0
# print(trinumW(-3)) # 0

# 2. Palindrome
def is_pal(s):
    return len(s) <= 1 or (s[0]==s[-1] and is_pal(s[1:-1]))

# print(is_pal("")) # True
# print(is_pal("a")) # True
# print(is_pal("aa")) # True
# print(is_pal("aba")) # True
# print(is_pal("abba")) # True
# print(is_pal("aaba")) # False
# print(is_pal("abcba")) # True
# print(is_pal("여보 안경 안 보여")) # False
# print(is_pal("여보안경안보여")) # True

# 3-A
def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def is_valid_date(year,month,day):
    return year > 0 and 1 <= month <= 12 and \
           (month in [1,3,5,7,8,10,12] and 1 <= day <= 31 or
            month in [4,6,9,11] and 1 <= day <= 30 or
            is_leap_year(year) and 1 <= day <= 29 or
            1 <= day <= 28)

def get_valid_date_6():
    s = input('Type 6 digits: ')
    if len(s) > 6: return None

    year = int(s[0:2])
    if year < 17:
        year += 2000
    else:
        year += 1900
    month = int(s[2:4])
    day = int(s[4:])

    if is_valid_date(year,month,day):
        return (year,month,day)
    else:
        return None

print(get_valid_date_6())

# 160425 # => (2016, 4, 25)
# 160431 # => None
# 160229 # => (2016, 2, 29)
# 170229 # => None
# 450815 # => (1945, 8, 15)

# 3-B
def next_month(year, month):
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return (year, month)

def days_in_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month in [2]:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 0

def date_plus(year, month, day, days):
    days_left = days_in_month(year,month) - day
    if days <= days_left:
        return (year, month, day+days)
    else:
        day = days - days_left
        year, month = next_month(year, month)

        while days_in_month(year, month) < day:
            day -= days_in_month(year, month)
            year, month = next_month(year, month)

        return (year, month, day)

# print(date_plus(2017,4,20,2)) # => (2017, 4, 22)
# print(date_plus(2017,4,20,7)) # => (2017, 4, 27)
# print(date_plus(2017,4,20,10)) # => (2017, 4, 30)
# print(date_plus(2017,4,20,11)) # => (2017, 5, 1)
# print(date_plus(2017,4,20,50)) # => (2017, 6, 9)
# print(date_plus(2017,4,20,100)) # => (2017, 7, 29)
# print(date_plus(2017,4,20,200)) # => (2017, 11, 6)
# print(date_plus(2017,4,20,300)) # => (2018, 2, 14)
# print(date_plus(2017,4,20,1000)) # => (2020, 1, 15)


# 4 문자열에서 특정 문자 모두 없애기
# 재귀함수
def remove(x,xs):
    if len(xs)>0:
        if xs[0]==x:
            return remove(x, xs[1:])
        else:
            return xs[0]+remove(x, xs[1:])
    else:
        return xs

# print(remove('a','abracadabra'))
# print(remove('z','abracadabra'))

# 꼬리재귀함수
def removeT(x,xs):
    def loop(xs, s):
        if len(xs)<=0:
            return s
        else:
            if xs[0]!=x:
                return loop(xs[1:], s+xs[0])
            else:
                return loop(xs[1:], s)
    return loop(xs, "")

# print(removeT('a','abracadabra'))
# print(removeT('z','abracadabra'))

# while 문 함수
def removeW(x,xs):
    i = 0
    l = len(xs)
    res=""
    while i < l:
        if xs[i] != x: res+=xs[i]
        i+=1
    return res

# print(removeW('a','abracadabra'))
# print(removeW('z','abracadabra'))

# 5. 순열
# recur
def permutation0(n,k):
    def loop(n,k):
        if k > 0:
            return n * loop(n-1,k-1)
        else:
            return 1
    if n < k:
        return 0
    else:
        return loop(n,k)

# tailRecur
def permutation1(n,k):
    def loop(n,k,p):
        if k > 0:
            return loop(n-1,k-1,p*n)
        else:
            return p
    if n < k:
        return 0
    else:
        return loop(n,k,1)

# while
def permutation2(n,k):
    if k>0:
        res=1; i=0
        while i<k:
            res *= n-i
            i+=1
        return res
    else:
        return 1

# for
def permutation3(n,k):
    if k > 0:
        res=1
        for i in range(k):
            res *= n-i
        return res
    else:
        return 1
# print(permutation3(1,1)) # => 1
# print(permutation3(2,1)) # => 2
# print(permutation3(2,2)) # => 2
# print(permutation3(3,1)) # => 3
# print(permutation3(4,3)) # => 24
# print(permutation3(4,4)) # => 24

def sublist(s, l, r):
    if l<0 or r<0:
        return []
    return s[l:r]

### A ###
# def drop_before(s,index):
#     while s != [] and index > 0:
#         s = s[1:]
#         index -= 1
#     return s

def drop_before(s,index):
    # 예시 코드
    # if s != [] and index > 0:
    #     return drop_before(s[1:],index-1)
    # else:
    #     return s
    res=[]
    if index<0: index=0
    while index<len(s):
        res.append(s[index])
        index+=1

    return res

# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("drop_before(s,0) =", drop_before(s,0)) # => [1,2,3,4,5]
# print("drop_before(s,1) =", drop_before(s,1)) # => [2,3,4,5]
# print("drop_before(s,-3) =", drop_before(s,-3)) # => [1,2,3,4,5]
# print("drop_before([],4) =", drop_before([],4)) # => []


### B ###
# recur
# def take_before(s,index):
#     if s == [] or index>=len(s):
#         return s
#     else:
#         return take_before(s[:index], index+1)
# def take_before(s,index):
#     if s != [] and index > 0:
#         return [s[0]] + take_before(s[1:],index-1)
#     else:
#         return []

# tail recur
def take_before(s,index):
    def loop(s, index, res):
        if s != [] and index > 0:
            res.append(s[0])
            return loop(s[1:], index - 1, res)
        else:
            return res
    return loop(s, index, [])

# while
# def take_before(s,index):
#     if index<=0:
#         return []
#     if index>len(s):
#         return s
#     res=[]; i=0
#     while i<index:
#         res.append(s[i])
#         i+=1
#     return res
#
# s = [1,2,3,4,5]
# print("take_before(s,0) =", take_before(s,0)) # => []
# print("take_before(s,1) =", take_before(s,1)) # => [1]
# print("take_before(s,2) =", take_before(s,2)) # => [1,2]
# print("take_before(s,3) =", take_before(s,3)) # => [1,2,3]
# print("take_before(s,4) =", take_before(s,4)) # => [1,2,3,4]
# print("take_before(s,5) =", take_before(s,5)) # => [1,2,3,4,5]
# print("take_before(s,6) =", take_before(s,6)) # => [1,2,3,4,5]
# print("take_before([],4) =", take_before([],4)) # => []
# print("take_before(s,-3) =", take_before(s,-3)) # => []

### C ###
def sublist(s,low,high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low <= high:
        return take_before(drop_before(s, low), high-low)
    else:
        return []
# s = [1,2,3,4,5]
# print("s = [1,2,3,4,5]")
# print("sublist(s,0,0) => [] ?", sublist(s,0,0))
# print("sublist(s,0,1) => [1] ?", sublist(s,0,1))
# print("sublist(s,0,2) => [1, 2] ?", sublist(s,0,2))
# print("sublist(s,0,3) => [1, 2, 3] ?", sublist(s,0,3))
# print("sublist(s,0,4) => [1, 2, 3, 4] ?", sublist(s,0,4))
# print("sublist(s,3,6) => [4, 5] ?", sublist(s,3,6))
# print("sublist(s,5,2) => [] ?", sublist(s,5,2))
# print("sublist(s,-3,-2) => [] ?", sublist(s,-3,-2))


# 7
### A ###
def longest_streak1(s):
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    index = 1
    for n in s[1:]:
        if n == contender:
            if streak_length == 1:
                contender_index = index
            streak_length += 1
        else:
            contender = n
            streak_length = 1
        if streak_length > streak_record:
            leader = contender
            streak_record = streak_length
            leader_index = contender_index

        index += 1
    return leader, streak_record, leader_index-1

# def test_longest_streak(s):
#     for n in s:
#         print(n,end="")
#     print()
#     print(longest_streak1(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0)
# # => ('0', 3, 15)
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1)
# # => ('5', 4, 15)
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2)
# # => ('8', 2, 19)
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3)
# # => ('8', 3, 2)


### B ###
def longest_streak2(s):
    res = []
    contender = leader = s[0]
    streak_length = streak_record = 1
    contender_index = leader_index = 0
    index = 1
    for n in s[1:]:
        if n == contender:
            if streak_length == 1:
                contender_index = index
            streak_length += 1
        else:
            contender = n
            streak_length = 1
        if streak_length > streak_record:
            leader = contender
            streak_record = streak_length
            leader_index = contender_index-1
            res = [(leader, streak_record, leader_index)]
        elif streak_length == streak_record:
            res.append((contender, streak_length, contender_index-1))
        index += 1

    return res

def test_longest_streak(s):
    for n in s:
        print(n,end="")
    print()
    print(longest_streak2(s))

# s0 = "06479019955907200041185008780528384811265678111671"
# test_longest_streak(s0)
# # => [('0', 3, 15), ('1', 3, 44)]
# s1 = "49715114250863455559013207228395154984882560834674"
# test_longest_streak(s1)
# # => [('5', 4, 15)]
# s2 = "79083787262159815638834042282485195270836937488097"
# test_longest_streak(s2)
# # => [('8', 2, 19), ('2', 2, 25), ('8', 2, 45)]
# s3 = "36888653851748777011129000999371447120618209984726"
# test_longest_streak(s3)
# # => [('8', 3, 2), ('7', 3, 14), ('1', 3, 18), ('0', 3, 23), ('9', 3, 26)]
