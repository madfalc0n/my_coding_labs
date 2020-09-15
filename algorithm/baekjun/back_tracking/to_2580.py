"""
백트래킹
수도쿠
https://www.acmicpc.net/problem/2580
"""
flag = False

def chk_ver(col,matrix):
    n_list = set(list(range(1,10)))
    m_list = set([matrix[i][col] for i in range(9)])
    return set(n_list - m_list)
        
def chk_hor(row,matrix):
    n_list = set(list(range(1,10)))
    m_list = set([matrix[row][i] for i in range(9)])
    return set(n_list - m_list)

def chk_seg(row,col,matrix):
    row_1 = (row // 3) * 3
    col_1 = (col // 3) * 3
    n_list = set(list(range(1,10)))

    m_list = set()
    for i in range(row_1, row_1 + 3):
        for j in range(col_1, col_1 + 3):
            m_list.add(matrix[i][j])
    return set(n_list - m_list)   



def bt(zero_list, matrix):
    global flag
    if flag:
        return
    if len(zero_list) == 0:
        for i in matrix:
            for j in i:
                print(j,end=' ')
            print()
        flag = True
        return
    else:
        cur = zero_list.pop(0)
        ver = chk_ver(cur[1],matrix) 
        hor = chk_hor(cur[0],matrix)
        seg = chk_seg(cur[0],cur[1],matrix)
        # print(ver,hor,seg)
        val_list = list(ver&hor&seg)
        if len(val_list) == 0:
            zero_list.insert(0,cur)
            return
        # print(val_list)
        for val in val_list:
            matrix[cur[0]][cur[1]] = val
            bt(zero_list, matrix)
            matrix[cur[0]][cur[1]] = 0
        if flag == False:
            zero_list.insert(0,cur)



matrix = [[0] * 9 for _ in range(9)]
v_matrix = [[0] * 9 for _ in range(9)]
# matrix= [
#     [0, 3, 5, 4, 6, 9, 2, 7, 8],
#     [7, 8, 2, 1, 0, 5, 6, 0, 9],
#     [0, 6, 0, 2, 7, 8, 1, 3, 5],
#     [3, 2, 1, 0, 4, 6, 8, 9, 7],
#     [8, 0, 4, 9, 1, 3, 5, 0, 6],
#     [5, 9, 6, 8, 2, 0, 4, 1, 3],
#     [9, 1, 7, 6, 5, 2, 0, 8, 0],
#     [6, 0, 3, 7, 0, 1, 9, 5, 2],
#     [2, 5, 8, 3, 9, 4, 7, 6, 0]
# ]

zero_list = list()
for i in range(9):
    matrix[i] = list(map(int, input().split(' ')))
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            zero_list.append([i,j])
bt(zero_list, matrix)


