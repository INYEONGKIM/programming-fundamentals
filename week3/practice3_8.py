def fastmult(m,n):
    ans = 0
    while n > 0:
        if n%2==0:
            m,n = 2*m, n//2
        else:
            n,ans = n-1, ans+m
    return ans