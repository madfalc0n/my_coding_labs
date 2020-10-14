"""
13460 번 구슬 탈출 2
https://www.acmicpc.net/problem/13460
중력을 이용해 빨간 구슬을 탈출시키는 문제
"""
def move(x,y,direction):
    global matrix
    global N,M
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    nx, ny = x,y
    cnt = 0
    while matrix[nx][ny] == '.':
        cnt += 1
        nx += dx[direction]
        ny += dy[direction]
        
    if matrix[nx][ny] == 'O':
        return [nx, ny,cnt]
        
    elif matrix[nx][ny] == '#':
        return [nx-dx[direction], ny-dy[direction],cnt]

    


def bfs(start, matrix):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visit = [start]
    queue = [start]
    cost = 1
    while queue and cost <= 10:
        for _ in range(len(queue)):
            rx,ry,bx,by = queue.pop(0)
            for i in range(4):
                nrx, nry, r_cnt = move(rx,ry,i)
                nbx, nby, b_cnt = move(bx,by,i)
            
                #파란색을 먼저 체크해서 들어갔으면 continue
                if matrix[nbx][nby] == 'O':
                    continue
                # 파란색 들어가지 않았고 빨간색만 들어갔을 경우 리턴
                elif matrix[nrx][nry] == 'O':
                    return cost
                # 둘다 안들어갔을때
                else:
                    if nrx == nbx and nry == nby:
                        if r_cnt < b_cnt:
                            nbx -= dx[i]
                            nby -= dy[i]
                        else:
                            nrx -= dx[i]
                            nry -= dy[i]
                    if [nrx,nry,nbx,nby] not in visit:
                        visit.append([nrx,nry,nbx,nby])
                        queue.append([nrx,nry,nbx,nby])
        cost += 1
    return -1

N,M = list(map(int,input().split()))
matrix = [['#'] * (M+1) for _ in range(N+1)]
for i in range(1,N+1):
    matrix[i] = ['#'] + list(input())

for i in range(1,N+1):
    for j in range(1,M+1):
        if matrix[i][j] == 'R':
            matrix[i][j] = '.'
            rx, ry = i,j
        elif matrix[i][j] == 'B':
            matrix[i][j] = '.'
            bx, by = i,j

#pr(matrix)
# print(rbo_dict)
start = [rx,ry,bx,by]
print(bfs(start, matrix))














# 틀린 나의 풀이
# def moving(rbo_dict, direction):
#     global matrix

#     # 상 하 좌 우
#     dx = [-1,1,0,0]
#     dy = [0,0,-1,1]

#     comp_dict = {
#         'R' : [0,0,0],
#         'B' : [0,0,0]
#     }
#     #방향먼저 보고 빨간공 파란공 누가 먼저 움직일건지 결정
#     while comp_dict['R'][0] == 0 or comp_dict['B'][0] == 0:
#         if direction == 0:
#             if rbo_dict['R'][1] > rbo_dict['B'][1]:
#                 move_list = [rbo_dict['B'] , rbo_dict['R']]
#                 name_list = ['B', 'R']
#             else:
#                 move_list = [rbo_dict['R'] , rbo_dict['B']]
#                 name_list = ['R', 'B']
#             for index in range(len(move_list)):
#                 tmp_name = name_list[index]
#                 if comp_dict[tmp_name][0] == 0:
#                     x,y = move_list[index][0], move_list[index][1]
#                     nx, ny = x + dx[direction], y + dy[direction]
#                     if nx in range(1,N+1) and ny in range(1,M+1):
#                         if matrix[nx][ny] == '.':
#                             matrix[x][y] = '.'
#                             matrix[nx][ny] = tmp_name
#                             rbo_dict[tmp_name] = [nx,ny]
#                         elif  matrix[nx][ny] == 'O': 
#                             matrix[x][y] = '.'
#                             comp_dict[tmp_name] = [1,nx,ny]
#                         else:
#                             comp_dict[tmp_name] = [-1,0,0]
#         elif direction == 1:
#             if rbo_dict['R'][1] < rbo_dict['B'][1]:
#                 move_list = [rbo_dict['B'] , rbo_dict['R']]
#                 name_list = ['B', 'R']
#             else:
#                 move_list = [rbo_dict['R'] , rbo_dict['B']]
#                 name_list = ['R', 'B']
#             for index in range(len(move_list)):
#                 tmp_name = name_list[index]
#                 if comp_dict[tmp_name][0] == 0:
#                     x,y = move_list[index][0], move_list[index][1]
#                     nx, ny = x + dx[direction], y + dy[direction]
#                     if nx in range(1,N+1) and ny in range(1,M+1):
#                         if matrix[nx][ny] == '.':
#                             matrix[x][y] = '.'
#                             matrix[nx][ny] = tmp_name
#                             rbo_dict[tmp_name] = [nx,ny]
#                         elif  matrix[nx][ny] == 'O': 
#                             matrix[x][y] = '.'
#                             comp_dict[tmp_name] = [1,nx,ny]
#                         else:
#                             comp_dict[tmp_name] = [-1,0,0]
#         elif direction == 2:
#             if rbo_dict['R'][0] > rbo_dict['B'][0]:
#                 move_list = [rbo_dict['B'] , rbo_dict['R']]
#                 name_list = ['B', 'R']
#             else:
#                 move_list = [rbo_dict['R'] , rbo_dict['B']]
#                 name_list = ['R', 'B']
#             for index in range(len(move_list)):
#                 tmp_name = name_list[index]
#                 if comp_dict[tmp_name][0] == 0:
#                     x,y = move_list[index][0], move_list[index][1]
#                     nx, ny = x + dx[direction], y + dy[direction]
#                     if nx in range(1,N+1) and ny in range(1,M+1):
#                         if matrix[nx][ny] == '.':
#                             matrix[x][y] = '.'
#                             matrix[nx][ny] = tmp_name
#                             rbo_dict[tmp_name] = [nx,ny]
#                         elif  matrix[nx][ny] == 'O': 
#                             matrix[x][y] = '.'
#                             comp_dict[tmp_name] = [1,nx,ny]
#                         else:
#                             comp_dict[tmp_name] = [-1,0,0]
#         elif direction == 3:
#             if rbo_dict['R'][0] < rbo_dict['B'][0]:
#                 move_list = [rbo_dict['B'] , rbo_dict['R']]
#                 name_list = ['B', 'R']
#             else:
#                 move_list = [rbo_dict['R'] , rbo_dict['B']]
#                 name_list = ['R', 'B']
#             for index in range(len(move_list)):
#                 tmp_name = name_list[index]
#                 if comp_dict[tmp_name][0] == 0:
#                     x,y = move_list[index][0], move_list[index][1]
#                     nx, ny = x + dx[direction], y + dy[direction]
#                     if nx in range(1,N+1) and ny in range(1,M+1):
#                         if matrix[nx][ny] == '.':
#                             matrix[x][y] = '.'
#                             matrix[nx][ny] = tmp_name
#                             rbo_dict[tmp_name] = [nx,ny]
#                         elif  matrix[nx][ny] == 'O': 
#                             matrix[x][y] = '.'
#                             comp_dict[tmp_name] = [1,nx,ny]
#                         else:
#                             comp_dict[tmp_name] = [-1,0,0]
#     return comp_dict

# def dfs(cost, rbo_dict):
#     global result_list
#     global overflow
#     # global same_come
#     red, blue = rbo_dict['R'], rbo_dict['B']

#     if cost == 10:
#         overflow = True
#     else:
#         #상 하 좌 우로 각각 증가 시키기
#         for i in range(4):
#             result = moving(rbo_dict, i)
#             if result['R'][0] == 1 and result['B'][0] == -1:
#                 result_list = min(cost, result_list)
#                 # print(result_list)
#                 return
#             dfs(cost + 1, rbo_dict)
#             for key in rbo_dict.keys():
#                 tmp_x, tmp_y = rbo_dict[key][0], rbo_dict[key][1]
#                 matrix[tmp_x][tmp_y] = '.'
#             matrix[red[0]][red[1]] = 'R'
#             matrix[blue[0]][blue[1]] = 'B'
#             rbo_dict['R'], rbo_dict['B'] = red, blue



# def pr(list):
#     for i in list:
#         print(i)

# N,M = list(map(int,input().split()))
# matrix = [['#'] * (M+1) for _ in range(N+1)]
# for i in range(1,N+1):
#     matrix[i] = ['#'] + list(input())

# rbo_dict = dict()
# for i in range(1,N+1):
#     for j in range(1,M+1):
#         if matrix[i][j] == 'R':
#             rbo_dict['R'] = [i,j]
#         elif matrix[i][j] == 'B':
#             rbo_dict['B'] = [i,j]

# #pr(matrix)
# # print(rbo_dict)
# cost = 0
# direction = -1
# result_list = 10
# overflow = False
# dfs(cost+1, rbo_dict)
# if overflow and result_list == 10:
#     print(-1)
# else:
#     print(result_list)



# 다른사람 풀이
# https://conak-diary.tistory.com/104

# def move(y, x, dirc):
#     ny = y + dy[dirc]
#     nx = x + dx[dirc]
#     distance = 0
#     while arr[ny][nx] == '.':
#         distance += 1
#         ny += dy[dirc]
#         nx += dx[dirc]
#     if arr[ny][nx] == 'O':
#         return ny, nx, distance
#     else:
#         return ny - dy[dirc], nx - dx[dirc], distance
 
 
# def BFS(Ry, Rx, By, Bx):
#     q = [(Ry, Rx, By, Bx)]
#     visited[Ry][Rx][By][Bx] = True
#     cnt = 1
#     while q and cnt <= 10:
#         for i in range(len(q)):
#             Ry, Rx, By, Bx = q.pop(0)
#             for dirc in range(4):
#                 nRy, nRx, R_move = move(Ry, Rx, dirc)
#                 nBy, nBx, B_move = move(By, Bx, dirc)
 
#                 if arr[nBy][nBx] == 'O':
#                     continue
#                 elif arr[nRy][nRx] == 'O':
#                     return cnt
#                 else:
#                     if nRy == nBy and nRx == nBx:
#                         if R_move > B_move:
#                             nRy -= dy[dirc]
#                             nRx -= dx[dirc]
#                         else:
#                             nBy -= dy[dirc]
#                             nBx -= dx[dirc]
 
#                         if not visited[nRy][nRx][nBy][nBx]:
#                             visited[nRy][nRx][nBy][nBx] = True
#                             q.append((nRy, nRx, nBy, nBx))
#                     else:
#                         if not visited[nRy][nRx][nBy][nBx]:
#                             visited[nRy][nRx][nBy][nBx] = True
#                             q.append((nRy, nRx, nBy, nBx))
#         cnt += 1
#     return -1
 
 
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
 
# N, M = map(int,input().split())
# arr = [list(input()) for _ in range(N)]
# visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'B':
#             By = i
#             Bx = j
#             arr[i][j] = '.'
#         elif arr[i][j] == 'R':
#             Ry = i
#             Rx = j
#             arr[i][j] = '.'
 
# print(BFS(Ry, Rx, By, Bx))