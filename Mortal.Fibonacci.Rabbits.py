from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1) if n < 4 else fib(n-2) + fib(n-1) - 1


print(fib(83))
print([fib(x) for x in range(1, 82)])
print(fib.cache_info())

