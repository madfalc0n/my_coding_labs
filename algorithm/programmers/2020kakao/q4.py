
user_list = []

# def bfs(start, matrix, visit_list, a):
#     visit_list.append(start)
#     queue = [start]
#     while queue:
#         cur = queue.pop(0)
#         for i in range(1, len(matrix[cur])):
#             if i not in visit_list and matrix[cur][i] != 0:
#                 queue.append(i)
#                 visit_list.append(i)
#                 if i == a:
#                     print(visit_list)
#                     return 

def check_price(a_list, b_list, matrix):
    len_a = len(a_list)
    len_b = len(b_list)
    
    #어디 까지 일치하는지 계산
    index = 0
    if len_a > len_b:
        for i in range(1, len_b):
            if a_list[i] == b_list[i]:
                index += 1
    else:
        for i in range(1, len_a):
            if a_list[i] == b_list[i]:
                index += 1
    sum_v = 0
    #print("index line")
    for i in range(1, index+1):
        #print(matrix[a_list[i-1]][a_list[i]])
        sum_v += matrix[a_list[i-1]][a_list[i]] 

    #print("pull_a_line")
    if len_a > index:
        for i in range(index+1, len_a):
            #print(matrix[a_list[i-1]][a_list[i]])
            sum_v += matrix[a_list[i-1]][a_list[i]]
    
    #print("pull_b_line")
    if len_b > index:
        for i in range(index+1, len_b):
            #print(matrix[b_list[i-1]][b_list[i]])
            sum_v += matrix[b_list[i-1]][b_list[i]]

    #print(a_list, b_list, index, sum_v)

    return sum_v

def dfs(start, matrix, visit_list, a):
    if start == a:
        cpy_list = visit_list.copy()
        user_list.append(cpy_list)
    else:
        for i in range(1, len(matrix[start])):
            if matrix[start][i] != 0 and i not in visit_list:
                visit_list.append(i)
                dfs(i, matrix, visit_list, a)
                visit_list.pop(-1)

def solution(n, s, a, b, fares):
    global user_list
    matrix = [[100001] * (n + 1) for _ in range(n+1)]
    visit = [0] * (n + 1)
    visit_list = []
    start = s
    
    #플로이드 워셜
    for i in fares:
        x,y,z = i[0], i[1], i[2]
        matrix[x][y] = z
        matrix[y][x] = z

    for i in range(len(matrix)):
        matrix[i][i] = 0

    for k in range(1, n+1): 
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    for i in matrix:
        print(i)

    # for i in fares:
    #     x,y,z = i[0], i[1], i[2]
        # matrix[x][y] = z
        # matrix[y][x] = z

    
    # visit_list = [start]
    # for i in range(1, len(matrix[start])):
    #     if matrix[start][i] != 0 and i not in visit_list: 
    #         bfs(i, matrix, visit_list, a)
    #         visit_list = [start]

    # visit_list = [start]
    # dfs(start, matrix, visit_list, a)
    # user_a_list = user_list
    # user_list = []
    # #print(sorted(user_a_list))

    # dfs(start, matrix, visit_list, b)
    # user_b_list = user_list
    # #print(sorted(user_b_list))

    # f = 100001
    # for i in user_a_list:
    #     for j in user_b_list:
    #         f = min(f,check_price(i, j, matrix))

    # return f

n,s,a,b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))

# n,s,a,b = 7, 3, 4, 1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# print(solution(n, s, a, b, fares))

