from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else (3 * fib(n-2)) + fib(n-1)


print(fib(29))
print([fib(x) for x in range(1, 30)])
print(fib.cache_info())

