def permutation(n,k):
    if k > 0:
        return (n-k+1)*permutation(n, k-1)
    else:
        return 1

def permutation(n,k):
    def loop(n,k,res):
        if k > 0:
            return loop(n,k-1,res*(n-k+1))
        else:
            return res
    return loop(n,k,1)

def permutation(n,k):
    res = 1
    while k>0:
        res *= (n-k+1)
        k -= 1
    return res

print(permutation(1,1)) # => 1
print(permutation(2,1)) # => 2
print(permutation(2,2)) # => 2
print(permutation(3,1)) # => 3
print(permutation(3,2)) # => 6
print(permutation(3,3)) # => 6
print(permutation(4,1)) # => 4
print(permutation(4,2)) # => 12
print(permutation(4,3)) # => 24
print(permutation(4,4)) # => 24