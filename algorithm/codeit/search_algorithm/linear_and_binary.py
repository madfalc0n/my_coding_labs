#선형 탐색
def linear_search(element, some_list):
    for i,num in enumerate(some_list):
        if num == element:
            return i
    return None

#이진 탐색
def binary_search(element, some_list):
    first_index = 0
    last_index = len(some_list)-1
    while 1:
        mid_index = (first_index+last_index)//2
        #print(first_index,mid_index , last_index)
        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] < element: #element가 mid index 값 보다 클 경우
            first_index = mid_index + 1    
        elif some_list[mid_index] > element: #element가 mid index 값 보다 작을 경우
            last_index = mid_index - 1
        if first_index > last_index: # last 인덱스가 first 인덱스보다 작을 경우 범위를 벗어난것으로 간주하여 None 리턴
            return None
        
#선형
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

#이진
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))