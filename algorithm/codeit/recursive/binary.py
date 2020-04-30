
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스

    if end_index == None:
        end_index = len(some_list) - 1
    if start_index > end_index: # over
        return None    
    mid_index = (start_index + end_index) // 2
    #print(start_index, mid_index, end_index)
    if some_list[mid_index] == element:
        return mid_index
    elif some_list[mid_index] < element:
        start_index = mid_index + 1
    elif some_list[mid_index] > element:
        end_index = mid_index - 1

    return binary_search(element, some_list, start_index, end_index)

    # 코드를 작성하세요.

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))