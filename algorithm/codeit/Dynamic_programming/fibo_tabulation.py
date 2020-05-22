# 메모리가 늘어나지 않는 공간복잡도 O(1) 방식
def fib_optimized(n):
    cur = 1
    pre = 0
    #print(cur, pre)
    for i in range(1,n+1):
        cur = cur + pre
        pre = cur 


    return cur

# 테스트
print(fib_optimized(4))
# print(fib_optimized(1))
# print(fib_optimized(2))
# print(fib_optimized(3))
# print(fib_optimized(4))
# print(fib_optimized(5))
# print(fib_optimized(16))
# print(fib_optimized(53))
# print(fib_optimized(213))




# 시간/공간 복잡도 O(n)
# def fib_tab(n):
#     tmp_list = [0] * (n+1)
#     for i in range(1,n+1):
#         if i == 1 or i == 2:
#             tmp_list[i] = 1
#         else:
#             tmp_list[i] = tmp_list[i-1] + tmp_list[i-2]
#     return tmp_list[n]

# # 테스트
# print(fib_tab(10))
# print(fib_tab(56))
# print(fib_tab(132))