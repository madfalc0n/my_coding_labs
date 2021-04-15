"""
이진 변환 반복하기
https://programmers.co.kr/learn/courses/30/lessons/70129
"""

def solution(s):
    answer = []
    cnt = 0
    cnt_2 = 0
    while len(s) > 1:
        del_zero = s.count('0')
        cnt += 1
        cnt_2 += del_zero
        s = bin(len(s)-del_zero)[2:]

    return [cnt,cnt_2]


# def lentobin(s):
#     # print(f"len {s}")
#     result = ''
#     while s > 1:
#         a = s // 2
#         b = s % 2
#         s = a
#         result += str(b)
#         # print(result)
#     result += str(s)
#     return result

# def solution(s):
#     answer = []
#     cnt = 0
#     cnt_2 = 0
#     while 1:
#         if len(s) == 1:
#             break
#         del_zero = 0
        
#         for i in s:
#             if i == '0':
#                 del_zero += 1
        
#         cnt += 1
#         cnt_2 += del_zero

#         # print(len(s), del_zero)
#         # s = lentobin(len(s)-del_zero)
#         s = bin(len(s)-del_zero)[2:]
    
#     return [cnt,cnt_2]


# print(solution("110010101001"))