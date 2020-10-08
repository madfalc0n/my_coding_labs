"""
쿼드트리
"""

def div_con(start, arr, len_arr):
    if len_arr == 1: 
        return arr[start[1]][start[0]]

    x,y = start[0], start[1]
    div_len_arr = len_arr // 2
    #1사분면 
    value_1 = div_con([x, y], arr, div_len_arr)
    #2사분면
    value_2 = div_con([x + div_len_arr, y], arr, div_len_arr)
    #3
    value_3 = div_con([x, y + div_len_arr], arr, div_len_arr)
    #4
    value_4 = div_con([x + div_len_arr, y + div_len_arr], arr, div_len_arr)

    tmp_list = []
    if type(value_1) == list:
        tmp_list.extend(value_1)
    else:
        tmp_list.append(value_1)
    if type(value_2) == list:
        tmp_list.extend(value_2)
    else:
        tmp_list.append(value_2)
    if type(value_3) == list:
        tmp_list.extend(value_3)
    else:
        tmp_list.append(value_3)
    if type(value_4) == list:
        tmp_list.extend(value_4)
    else:
        tmp_list.append(value_4)

    print(x,y,tmp_list)
    if tmp_list.count(1) == 4:
        return [1]
    elif tmp_list.count(0) == 4:
        return [0]
    else:
        return [value_1] + [value_2] + [value_3] + [value_4]

    # val_list = [value_1, value_2, value_3, value_4]
    # print(x,y,val_list)
    # if val_list.count(1) == 4:
    #     return [1]
    # elif val_list.count(0) == 4:
    #     return [0]
    # else:
    #     return val_list

def solution(arr):
    if len(arr) == 1:
        if arr[0] == 1:
            return [0,1]
        else:
            return [1,0]
    
    len_arr = len(arr)
    val_list = div_con([0,0], arr, len_arr)
    print("val_list")
    print(val_list[0])
    print(len(val_list[0]))
    
    return [val_list.count(0),val_list.count(1)]

# arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# print(solution(arr))

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))