# 성공

def recur(start, sum_val, s_index, e_index, row, matrix, n):
    if start > sum_val:
            return 

    for i in range(s_index, n):
        if start > sum_val:
            return 
        matrix[i].insert(row,start)
        start += 1

    for i in range(n + e_index):
        if start > sum_val:
            return
        tmp_index =  row + 1 + i
        matrix[n-1].insert(tmp_index, start)
        start += 1

    for i in range(n-2, s_index, -1):
        if start > sum_val:
            return
        tmp_len = len(matrix[i]) 
        matrix[i].insert(tmp_len - row, start)
        start += 1
    
    
    recur(start, sum_val, s_index+2, e_index-2, row+1, matrix, n-1)



def solution(n):
    sum_val = int((n*(n+1)) /2)
    matrix = [list() for _ in range(n)]
    #print(matrix)
    start = 1
    row = 0
    s_index = 0
    e_index = -1
    recur(start, sum_val, s_index, e_index, row, matrix, n)

    for i in matrix:
        print(i)

    result = []
    for i in matrix:
        result.extend(i)

    return result

n = 10
print(solution(n))
