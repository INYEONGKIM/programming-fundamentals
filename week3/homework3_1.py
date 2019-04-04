def square(n):
    def loop(n):
        if n > 0:
            return 2*n-1 + loop(n-1)
        else:
            return 0
    return loop(abs(n))

def square(n):
    def loop(n, res):
        if n>0:
            return loop(n-1, res+(2*n-1))
        else:
            return res
    return loop(abs(n), 0)

def square(n):
    n = abs(n)
    res=0
    while n>0:
        res += (2*n-1)
        n-=1
    return res

print(square(0)) # => 0
print(square(1)) # => 1
print(square(-2)) # => 4
print(square(3)) # => 9
print(square(-4)) # => 16
print(square(5)) # => 25

