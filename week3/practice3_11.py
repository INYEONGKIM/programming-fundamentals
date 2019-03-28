def rsmult(m,n):
    res=0
    while n>=1:
        if n%2==1:
            res+=m
        m *= 2
        n //= 2
    return res