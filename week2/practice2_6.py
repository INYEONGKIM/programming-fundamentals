def isinteger(s):
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()

def isfloat(x):
    s = x.partition(".")
    if s[1]=='.':
        if s[0]=='' or s[0]=='-':
            if s[2]=='' or s[2][0]=='-':
                return False
            else:
                return isinteger(s[2])
        elif isinteger(s[0]):
            if s[2]!='' and s[2][0]=='-':
                return False

            return s[2]=='' or isinteger(s[2])
        else:
            return False
    else:
        return False

print(isfloat(".112"))
print(isfloat("-.112"))
print(isfloat("3.14"))
print(isfloat("-3.14"))
print(isfloat("-3.14"))
print(isfloat("5.0"))
print(isfloat("-777.0"))
print(isfloat("-777."))
print(isfloat("."))
print(isfloat(".."))
print(isfloat("-21.-1"))
print(isfloat("-.-1"))
