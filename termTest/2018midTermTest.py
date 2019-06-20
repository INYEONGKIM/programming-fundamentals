# 1 9의 보수 구하기
# def complement9(n):
#     s = str(n)
#     ans = ""
#     for c in s:
#         ans += str(9-(ord(c)-ord('0')))
#     return int(ans)

def complement9(n):  # 자연수라고 가정
    s = str(n)
    ans = ""
    for c in s:
        ans += str(9-int(c))
    return int(ans)

print(complement9(0)) # 9
print(complement9(9)) # 0
print(complement9(4)) # 5
print(complement9(18)) # 81
print(complement9(40)) # 59
print(complement9(307)) # 692
print(complement9(9965)) # 34

# 2 찾기
def search(key,ns):
    res=[]
    for i in range(len(ns)):
        if ns[i]==key:
            res.append(i)
    return res

print(search(3,[])) # []
print(search(3,[4,6,3,3,3])) # [2,3,4]
print(search(3,[3,3,3,3,3])) # [0,1,2,3,4]
print(search(3,[4,2,7,6,5])) # []

# 3 올려세는 리스트 만들기(꼬리재귀버전)
def count_upto(n):
    def loop(n,ns):
        if n < 0:
            return ns+[]
        else:
            return loop(n-1, ns+[n])
    return loop(n,[])


print(count_upto(0)) # [0]
print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
print(count_upto(-3)) # []

# 4 올려세는 리스트 만들기(while)
def count_upto(n):
    ns = []
    while n>=0:  # 이 부분을 채우자
        ns.append(n)
        n-=1
    return ns

print(count_upto(0)) # [0]
print(count_upto(5)) # [0, 1, 2, 3, 4, 5]
print(count_upto(-3)) # []

# 5 리스트 원소별 더하기(꼬리재귀버전)
def zippo(xs, ys):
    def loop(xs, ys, zs):
        if xs == [] or ys == []:
            return zs + xs + ys
        else:
            return loop(xs[1:], ys[1:], zs+[xs[0]+ys[0]])

    return loop(xs, ys, [])

print(zippo([], []))  # []
print(zippo([2, 7, 4], [7, 2, 5]))  # [9,9,9]
print(zippo([2, 7, 4], [7, 2, 5, 9, 9]))  # [9,9,9,9,9]
print(zippo([2, 7, 4, 9, 9], [7, 2, 5]))  # [9,9,9,9,9]

# 6 리스트 원소별 더하기(while)
def zippo(xs, ys):
    zs = []
    while xs!=[] and ys!=[]:  # 이 부분을 채우자
        zs += [xs[0]+ys[0]]
        xs = xs[1:]
        ys = ys[1:]
    return zs + xs + ys

print(zippo([], []))  # []
print(zippo([2, 7, 4], [7, 2, 5]))  # [9,9,9]
print(zippo([2, 7, 4], [7, 2, 5, 9, 9]))  # [9,9,9,9,9]
print(zippo([2, 7, 4, 9, 9], [7, 2, 5]))  # [9,9,9,9,9]

# 7 Blast
def blast(ns):
    bs = []
    for i in ns:
        if i>0:
            for j in range(0,i):
                bs+=[i]
    return bs

print(blast([3,5]))
print(blast([2,-3,3]))


# 8 합집합
def makeset(xs):
    ys = []
    for x in xs:
        if x not in ys:
            ys.append(x)
    return ys

import random

s1 = makeset([random.randrange(10) for _ in range(10)])
print(s1)
s2 = makeset([random.randrange(10) for _ in range(10)])
print(s2)

def union(xs,ys):
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs+ys
# def union(xs,ys):
#     return list(set(xs+ys))

print(union(s1, s2))
print(union([3,2,4],[1,2,3]))

# 9 차집합
def diff(xs,ys):
    res=[]
    for i in xs:
        if i not in ys:
            res += [i]
    return res

print(diff(s1, s2))
print(diff([3,2,4],[1,2,3]))

# 10 교집합
def intersect(xs,ys):
    res=[]
    for i in ys:
        if i in xs:
            res += [i]
    return res

print(intersect(s1, s2))
print(intersect([3,2,4],[1,2,3]))

# 11 Equivalent class
def equiv_class(ns):
    ns.sort()
    if ns == []:
        return []
    else:
        top = ns[0]
        nss = [[top]]
        for n in ns[1:]:
            idx = len(nss)-1
            if top == n:
                nss[idx].append(n)
            else:
                top = n
                nss += [[top]]

        return nss

print(equiv_class([]))
print(equiv_class([3]))
print(equiv_class([4,3,2,4,4]))
print(equiv_class([2,4,4,2,2,3]))

# 12 Permutation
import math

def perm(l):
    if len(l)==0:
        return []

    res=[]
    for i in range(int(math.pow(2,len(l)))):
        r=[]
        temp = bin(i)[2:]
        while len(temp)<len(l):
            temp='0'+temp
        temp = temp[::-1]
        for i in range(len(temp)):
            if temp[i]=='1':
                r.append(l[i])
        res+=[r]
    return res

print(perm([]))
print(perm([1]))
print(perm([1,2]))
print(perm([1,2,3]))
print(perm([1,2,3,4]))


