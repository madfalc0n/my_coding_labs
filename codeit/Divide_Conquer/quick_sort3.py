def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list

def partition(my_list, start, end):
    #print("변경전 마이리스트,",my_list, start,end)
    pivot = my_list[end]
    big = start
    #print(f"pivot : {pivot}, unknown : {unknown} ")
    for i in range(start,end):
        if my_list[i] < pivot:
            my_list = swap_elements(my_list,big,i)
            big += 1 
    
    #print(f"big : {big}, mylist : {my_list}")
    my_list= swap_elements(my_list,big,end)
    #print("변경된 마이리스트,",my_list, start,end)
    pivot_index = big
    return pivot_index


# 퀵 정렬
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) -1
    #print(start,end,my_list)
    if  end - start < 1:
        return my_list
    pivot_num = partition(my_list, start, end)
    #print("pivot. ",pivot_num, my_list)
    quicksort(my_list,start,pivot_num-1)
    quicksort(my_list,pivot_num+1,end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)