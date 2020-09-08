"""
타겟넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
"""

# def dfs(numbers, target, change_v, val_list ,cur=0):
#     if change_v == cur:
#         if sum(numbers) - sum(val_list[1::]) == target:
#             val_list[0] += 1
#     else:
#         for i in range(len(numbers)):
#             tmp_val = numbers.pop(0)
#             val_list.append(tmp_val)
#             if sum(val_list[1::]) > target:
#                 break
#             print(f"val_list : {val_list} change_v : {change_v}  numbers : {numbers}")
#             dfs(numbers, target, change_v, val_list ,cur + 1)
#             val_list.pop(-1)
#             numbers.append(tmp_val)

# def solution(numbers, target):
#     val_list = [0]
#     if sum(numbers) == target:
#         return 1
#     for i in range(1, len(numbers)):
#         dfs(numbers, target, i, val_list)
#     # print(val_list)
#     return val_list[0]



# numbers	= [1,2,1,2,1]
# target = 3

# print(solution(numbers, target))


# 트리 이용한 탐색
# def solution(numbers, target):
#     answer_list = [0]
#     for i in numbers:
#         temp_list = []
#         for j in answer_list:
#             temp_list.append(j+i)
#             temp_list.append(j-i)
#         answer_list=temp_list
#         print(answer_list)
#     answer = answer_list.count(target)
#     return answer

# numbers	= [1,2,1,2,1]
# target = 3

# print(solution(numbers, target))

#재귀를 이용한 미친 다른풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])