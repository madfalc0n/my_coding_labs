
# 공식적용한 답
"""
모든 경우의 수 구하는 공식
(종류1개수 + 1) * (종류2개수 + 1) * (종류n개수 +1) -1 = 모든 경우의 수
"""
def solution(clothes):
    dict = {}
    for data in clothes:
        dict[data[1]] = dict.get(data[1],0) +1

    list_val = list(dict.values())
    
    answer = 1
    for data in list_val:
        answer *= data+1 

    answer -= 1

    return answer


clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print(solution(clothes))


# 시간초과
# from itertools import combinations,permutations
# from functools import reduce

# def solution(clothes):
#     dict = {}
#     answer = 0
#     for data in clothes:
#         dict[data[1]] = dict.get(data[1],0) +1

#     list_val = dict.values()
#     list_key = dict.keys()
#     answer = sum(list_val) # 1개씩만 입었을 때 값
#     len_key = len(list_key)

#     if len_key > 1: #항목이 2개 이상일 경우 

#         for i in range(2,len_key+1):
#             #print(f"index : {i}")
#             tmp_list = list(combinations(list(list_val),i))
#             #print(f"tmp_list : {tmp_list}")
#             for data in tmp_list:      
#                 tmp = reduce(lambda x, y: x * y, data)
#                 #print(f"tmp : {tmp}, data : {data}")
#                 answer += tmp


#     #print(dict)

#     return answer


# clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# print(solution(clothes))