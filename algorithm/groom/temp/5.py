

def bfs(cur_p, matrix):
    # down, r
    dx = [1,0,-1,0]
    dy = [0,1,0,1]
    tx,ty = cur_p
    queue = [cur_p]
    v_list = [cur_p]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= n and 0 < ny <= m:
                if [nx,ny] not in v_list:
                    matrix[nx][ny] = max(matrix[x][y]+matrix[nx][ny], matrix[nx][ny])
                    queue.append([nx,ny])
                    v_list.append([nx,ny])
                    print(v_list)

m,n = list(map(int,input().split(' ')))
# print(n,m)

matrix = [[0] * (m + 1) for _ in range(n+1)]

for i in range(1,n+1):
    matrix[i] = [0] + list(map(int,input().split(' ')))

result_list = [] 
org_matrix = matrix.copy()
bfs([1,1], matrix)

# print(max(result_list))
print(matrix[n][m])

# def dfs(cur_p, matrix,v_list, point):
#     # down, r
#     dx = [1,0]
#     dy = [0,1]
#     tx,ty = cur_p
#     v_list.append([tx,ty])
#     point += matrix[tx][ty]
#     if tx == n and ty == m:
#         result_list.append(point)
#     else:
#         for i in range(2):
#             nx = tx + dx[i]
#             ny = ty + dy[i]
#             if 0 < nx <= n and 0 < ny <= m:
#                 if [nx,ny] not in v_list:
#                     dfs([nx,ny], matrix, v_list, point)
#                     v_list.pop(-1)


# m,n = list(map(int,input().split(' ')))
# # print(n,m)

# matrix = [[0] * (m + 1) for _ in range(n+1)]

# for i in range(1,n+1):
#     matrix[i] = [0] + list(map(int,input().split(' ')))

# result_list = [] 
# v_list = []
# dfs([1,1], matrix,v_list, 0)

# print(max(result_list))