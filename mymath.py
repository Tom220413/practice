def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)

def fib_l(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    for  _ in range(n - 1):
        a,b = b,a + b
    return b

def fib_m(n, memo=None):
    if not memo:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib_m(n - 2, memo) + fib_m(n - 1, memo)
    return memo[n]
