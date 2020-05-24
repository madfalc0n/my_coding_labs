def fib_optimized(n):
    cur = 1
    pre = 1
    #print(cur, pre)
    for i in range(1,n+1):
        if i == 1 or i == 2:
            cur = 1
        else:
            cur = pre + cur
            pre = cur

    return cur

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
