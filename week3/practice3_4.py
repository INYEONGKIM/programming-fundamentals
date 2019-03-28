def mult1(m,n):
    def loop(n,ans):
        if n > 0:
            return loop(n-1, ans+m)
        else:
            return ans
    return loop(n,0)