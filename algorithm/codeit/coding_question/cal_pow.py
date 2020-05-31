"""
거듭제곱
 시간복잡도를 O(log(y)) 로 바꿔보자
 재귀적인 O(y)O(y) 솔루션은 문제 크기를 1씩 줄여 나가자만 O(log(y))를 위해서는 문제를 나누어야한다. 
"""
# #O(log(y))
def power(x, y):
    if y == 1:
        return x

    subresult = power(x, y//2)

    if y%2 == 0 : #짝수일때
        return subresult * subresult
    else: #홀수일떄
        return x * subresult * subresult

    

# #O(y)
# def power(x, y):
#     val = x
#     if y == 1:
#         return x
#     return val * power(x,y-1)


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))