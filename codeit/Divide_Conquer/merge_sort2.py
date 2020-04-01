#내가짠 코드, 디바이드 콘커 사용x
def merge(list1, list2):
    # 코드를 작성하세요.
    #print(list1, list2)
    len_l1 = len(list1)
    len_l2 = len(list2)
    result = []
    for _ in range(len_l1+len_l2):
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


# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) == 1:
        return my_list

    mid_len = len(my_list) // 2
    merge1 = merge_sort(my_list[:mid_len])
    merge2 = merge_sort(my_list[mid_len:])
    merge3 = merge(merge1,merge2) # 정렬 해주는 놈

    return merge3
    

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
