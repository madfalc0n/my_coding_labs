#내가짠 코드, 디바이드 콘커 사용x
def merge(list1, list2):
    # 코드를 작성하세요.
    #print(list1, list2)
    len_l1 = len(list1)
    len_l2 = len(list2)
    result = []
    for i in range(len_l1+len_l2):
        #print(i)
        #print(result)
        #print(len(list1), len(list2))
        if len(list1) == 0 :
            result.append(list2.pop(0))
            continue
        elif len(list2) == 0:
            result.append(list1.pop(0))
            continue

        if list1[0] >= list2[0]:
            result.append(list2.pop(0))
        else:
            result.append(list1.pop(0))

    return result



    
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))



#베스트케이스? 재귀를 사용하지 않음
# def merge(list1, list2):
#     i = 0
#     j = 0

#     # 정렬된 항목들을 담을 리스트
#     merged_list = []

#     # list1과 list2를 돌면서 merged_list에 항목 정렬
#     while i < len(list1) and j < len(list2):
#         if list1[i] > list2[j]:
#             merged_list.append(list2[j])
#             j += 1
#         else:
#             merged_list.append(list1[i])
#             i += 1

#     # list2에 남은 항목이 있으면 정렬 리스트에 추가
#     if i == len(list1):
#         merged_list += list2[j:]

#     # list1에 남은 항목이 있으면 정렬 리스트에 추가
#     elif j == len(list2):
#         merged_list += list1[i:]

#     return merged_list

# # 테스트
# print(merge([1],[]))
# print(merge([],[1]))
# print(merge([2],[1]))
# print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
# print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
# print(merge([4, 7, 8, 9],[1, 3, 6, 10]))