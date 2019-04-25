# 1
def flatten(xss):
    flat = []
    for x in xss:
        if isinstance(x,list):
            flat += flatten(x)
        else:
            flat.append(x)
    return flat
# print(flatten([[[[3]],[4]],5,6,[7]]))

# 2
def identity(mat):
    size = len(mat)
    for i in range(size):
        for j in range(size):
            if i==j:
                if mat[i][j]!=1: return False
            else:
                if mat[i][j]!=0: return False
    return True
# xs0 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
# xs1 = [[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]]
# xs2 = [[0,-3,6,4],[3,0,-9,8],[-6,9,0,2],[-4,-8,-2,0]]
# print(identity(xs0))
# print(identity(xs1))
# print(identity(xs2))

# 3
def ascii_art_cross(n):
    mid = ""
    el = ""
    center = n//2
    for i in range(n):
        mid+="#"
        if i == center:
            el+="#"
        else:
            el+=" "
    for i in range(n):
        if i == center:
            print(mid)
        else:
            print(el)

def ascii_art_square(n):
    top = ""
    mid = ""
    for i in range(n):
        if i==0 or i==n-1:
            mid+="#"
        else:
            mid+=" "
        top+="#"
    for i in range(n):
        if i==0 or i==n-1:
            print(top)
        else:
            print(mid)

def ascii_art_X(n):
    center = n//2
    for i in range(center+1):
        for j in range(i):
            print(" ",end="")
        print("#", end="")
        for j in range(n-2-2*i):
            print(" ", end="")
        if i != center:
            print("#")
        else:
            print()
    for i in range(center):
        for j in range(center-i-1):
            print(" ", end="")
        print("#", end="")
        for j in range(2*i+1):
            print(" ", end="")
        print("#")

def ascii_art_diamond(n):
    center = n//2
    for i in range(center):
        for j in range(center-i):
            print(" ",end="")
        print("#", end="")
        for j in range(2*i-1):
            print(" ", end="")
        if i!=0:
            print("#")
        else:
            print()
    for i in range(center+1):
        for j in range(i):
            print(" ",end="")
        print("#", end="")
        for j in range(center - 2*(i-1)):
            print(" ", end="")
        if i!=center:
            print("#")
        else:
            print()

# print(ascii_art_cross(7))
# print(ascii_art_square(5))
# print(ascii_art_X(7))
# print(ascii_art_diamond(7))

# 4
def substrings_of_length(length,s):
    if length == 0: return ['']
    if len(s)<length: return None
    res=[]
    start = 0
    end = start+length
    while end<=len(s):
        res.append(s[start:end])
        start+=1
        end = start+length
    return res
# print(substrings_of_length(0,"ERICA"))
# print(substrings_of_length(1,"ERICA"))
# print(substrings_of_length(2,"ERICA"))
# print(substrings_of_length(3,"ERICA"))
# print(substrings_of_length(4,"ERICA"))
# print(substrings_of_length(5,"ERICA"))
# print(substrings_of_length(6,"ERICA"))

def substrings(s):
    size = len(s)
    res=[]
    for i in range(size+1):
        res.append(substrings_of_length(i, s))

    def flatten(xss):
        flat = []
        for x in xss:
            if isinstance(x, list):
                flat += flatten(x)
            else:
                flat.append(x)
        return flat
    res = flatten(res)
    return res
# print(substrings("ERICA"))

# 5
def longest_ascending_sublist(l):
    res = sublist = [l[0]]
    length = len(l)
    start = l[0]
    for i in range(1,length):
        if start < l[i]:
            sublist.append(l[i])
        else:
            if len(res) < len(sublist):
                res = sublist
            sublist = [l[i]]
        start = l[i]
    return res

def longest_steepest_ascending_sublist(l):
    res = sublist = [l[0]]
    length = len(l)
    start = l[0]
    for i in range(1, length):
        if start < l[i]:
            sublist.append(l[i])
        else:
            if len(res) < len(sublist):
                res = sublist
            elif len(res) == len(sublist):
                if (res[len(res) - 1] - res[0]) / len(res) < (sublist[len(sublist) - 1] - sublist[0]) / len(sublist):
                    res = sublist
            sublist = [l[i]]
        start = l[i]
    return res
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63,98,59,7,23,34,67,77,30,49,55,31,58,10,27,15,45,42,77,11,14,9,55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_ascending_sublist(sample))
# print(longest_ascending_sublist([1,5,3,4,8,2,3,5]))
#
# print(longest_steepest_ascending_sublist(sample))
