from decorators.timing import measure_time


dp = dict()


# Introducing undecorated _f here so only time taken for overall f is printed
def _f(n: int) -> int:

    if n == 0 or n == 1:
        return n

    if n not in dp:
        dp[n] = _f(n - 1) + _f(n - 2)

    return dp[n]


@measure_time
def f(n: int) -> int:
    """Returns the nth Fibonacci number"""

    if n == 0 or n == 1:
        return n

    if n not in dp:
        dp[n] = _f(n - 1) + _f(n - 2)

    return dp[n]


for nth in (3, 5, 8, 21, 100, 888, 1337):

    print(f"Fibonacci number {nth}: {f(nth)}")
    print()
