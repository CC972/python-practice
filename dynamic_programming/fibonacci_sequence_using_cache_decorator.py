from functools import cache


@cache
def f(n: int) -> int:
    """Returns the nth Fibonacci number"""

    if n == 0 or n == 1:
        return n

    return f(n - 1) + f(n - 2)


print(f(8))
print(f(200))
