

def dfs(cur_p, matrix, v_list, point):
    # down, r, l
    dx = [1,0,0]
    dy = [0,1,-1]
    tx,ty = cur_p
    if tx == n:
        if matrix[tx][ty] == '.':
            result_list.append(point)
        elif matrix[tx][ty] == 'x':
            result_list.append(-1)
    else:
        v_list.append([tx,ty])
        for i in range(3):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 < nx <= n and 0 < ny <= m:
                if [nx,ny] not in v_list and matrix[nx][ny] == '.':
                    if i >0:
                        dfs([nx,ny], matrix, v_list, point+1)
                    elif i == 0 :
                        dfs([nx,ny], matrix, v_list, point)
                    

m,n = list(map(int,input().split(' ')))
# print(n,m)

matrix = [[0] * (m + 1) for _ in range(n+1)]

c_p = []
for i in range(1,n+1):
    matrix[i] = [0] + list(input())
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'c':
            c_p.append([i,j])

result_list = [] 
for cur_p in c_p:
    v_list = []
    point = 0
    dfs(cur_p, matrix, v_list, point)

print(min(result_list))



# def dfs(cur_p, matrix, v_list, point):
#     # down, r, l
#     dx = [1,0,0]
#     dy = [0,1,-1]
#     tx,ty = cur_p
#     if tx == n:
#         if matrix[tx][ty] == '.':
#             result_list.append(point)
#         elif matrix[tx][ty] == 'x':
#             result_list.append(-1)
#     else:
#         v_list.append([tx,ty])
#         for i in range(3):
#             nx = tx + dx[i]
#             ny = ty + dy[i]
#             if 0 < nx <= n and 0 < ny <= m:
#                 if [nx,ny] not in v_list and matrix[nx][ny] == '.':
#                     if i >0:
#                         dfs([nx,ny], matrix, v_list, point+1)
#                     elif i == 0 :
#                         dfs([nx,ny], matrix, v_list, point)
                    

# m,n = list(map(int,input().split(' ')))
# # print(n,m)

# matrix = [[0] * (m + 1) for _ in range(n+1)]

# c_p = []
# for i in range(1,n+1):
#     matrix[i] = [0] + list(input())
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == 'c':
#             c_p.append([i,j])

# result_list = [] 
# for cur_p in c_p:
#     v_list = []
#     point = 0
#     dfs(cur_p, matrix, v_list, point)

# print(min(result_list))