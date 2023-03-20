#! python
import timeit


# 일반적인 피보나치 수열
def fibonacci(n):
    if n in (0, 1):
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# dict을 이용한 memoization
def memoization_fibo(n, memo={}):
    #print(memo)
    if n in (0, 1):
        return n

    if n in memo:
        return memo[n]
    else:
        result = memoization_fibo(n - 1, memo) + memoization_fibo(n - 2, memo)
        memo[n] = result
        return result
    pass


# decorator를 이용한 memoization
# decorator를 사용하는 경우가 코드 파악이 쉽다.
def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return memoized_func


@memoize
def fibo(n):
    if n in (0, 1):
        return n

    return fibo(n - 1) + fibo(n - 2)


print("Not memoization")
t1 = timeit.Timer("fibonacci(35)", "from __main__ import fibonacci")
print(t1.timeit(1))
print('-' * 30)

print("Normal memoization")
t1 = timeit.Timer("memoization_fibo(35)", "from __main__ import memoization_fibo")
print(t1.timeit(1))
print('-' * 30)

print("decorator memoization")
t1 = timeit.Timer("fibo(35)", "from __main__ import fibo")
print(t1.timeit(1))
print('-' * 30)
