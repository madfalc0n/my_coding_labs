"""
제곱수 임의로 더한거
1, 3, 4, 9, 10, 12, 13, 27, 28,,,
"""
def solution(n):
    start_index = 3
    start_squared = 2
    tmp_list = [0,1,3]
    while start_index < n:
        if n == 1:
            return 1
        elif n == 2:
            return 3
        else:
            sum_list = [val+tmp_list[-1] for val in tmp_list[1:-1]]
            #print(sum_list)
            tmp_list += sum_list
            tmp_list.append(3**start_squared)
        #print(tmp_list)
        if len(tmp_list) >= n:
            return tmp_list[n]
        start_index += 1
        start_squared += 1

n = 11
print(solution(n))