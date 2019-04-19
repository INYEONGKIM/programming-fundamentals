# def minsteps1(n):
#     memo = [0] * (n + 1)
#     def loop(n):
#         if n > 1:
#             if memo[n] != 0:
#                 return memo[n]
#             else:
#                 memo[n] = 1 + loop(n - 1)
#                 if n % 2 == 0:
#                     memo[n] = min(memo[n], 1 + loop(n // 2))
#                 if n % 3 == 0:
#                     memo[n] = min(memo[n], 1 + loop(n // 3))
#                 return memo[n]
#         else:
#             return 0
#     return loop(n)

def minsteps(n):
    memo = [0] * (n + 1)
    for i in range(1, n+1):
        memo[i] = 1 + memo[i-1]
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i // 2]+1)
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i // 3]+1)
    # print(memo[1:])
    return memo[n]-1

print(minsteps(10)) # 3
print(minsteps(317)) # 10
print(minsteps(514)) # 8
