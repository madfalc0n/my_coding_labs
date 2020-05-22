"""
n번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.
fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!
"""

def fib_memo(n, cache):
    if n == 1 or n == 2:
        cache[n] = 1
        return cache[n]

    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_memo(n-1,cache) + fib_memo(n-2,cache)
        return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))