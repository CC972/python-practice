dp = dict()


def f(n: int) -> int:
    """Returns the nth Fibonacci number"""

    if n == 0 or n == 1:
        return n

    if n not in dp:
        dp[n] = f(n - 1) + f(n - 2)

    return dp[n]


print(f(8))
print(f(200))
