"""
연구소3
https://www.acmicpc.net/problem/17142
"""
from itertools import combinations

def bfs(v_point):
    global matrix
    global N
    global min_val
    global zero_cnt

    copy_matrix = [[0] * N for _ in range(N)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0: #벽일떄
                copy_matrix[i][j] = 0
            elif matrix[i][j] == 1: #벽일떄
                copy_matrix[i][j] = '-'
            else: #바이러스 일때
                copy_matrix[i][j] = '*'

    visit = []
    queue = []
    for point in v_point:
        tmp_x, tmp_y = point[0], point[1]
        visit.append([tmp_x,tmp_y])
        queue.append([tmp_x,tmp_y,0])
        copy_matrix[tmp_x][tmp_y] = '@'
        
    max_val = 0
    tmp_zero_cnt = 0
    over_val = False
    while queue:
        x,y,cost = queue.pop(0)
        if over_val:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(N) and ny in range(N) and copy_matrix[nx][ny] in range(N**2):
                if [nx,ny] not in visit:
                    copy_matrix[nx][ny] = cost + 1
                    max_val = max(max_val,copy_matrix[nx][ny])
                    queue.append([nx,ny,copy_matrix[nx][ny]])
                    visit.append([nx,ny])
                    tmp_zero_cnt += 1
                    if max_val > min_val:
                        over_val = True
                        break

    if zero_cnt == tmp_zero_cnt:
        min_val = min(min_val, max_val)

    # spread = True
    # for i in copy_matrix:
    #     if i.count(0):
    #         spread = False
    # if spread:
    #     min_val = min(min_val, max_val)
     

def dfs(v_point, cost, v_point2):
    global matrix
    global M

    if cost == M:
        #bfs 작업개시
        # print(v_point2)
        bfs(v_point2)
    else:
        for i in range(len(v_point)):
            v_point2.append(v_point.pop(i))
            dfs(v_point, cost+1, v_point2)
            v_point.insert(i,v_point2.pop(-1))
            

N, M = list(map(int,input().split()))
matrix = [ list(map(int,input().split())) for _ in range(N) ]

v_point = []
zero_cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            v_point.append([i,j])
        elif matrix[i][j] == 0:
            zero_cnt += 1
# print(v_point)
min_val = N**2
cost = 0
v_point2 = []
# dfs(v_point,cost,v_point2)
for point in combinations(v_point,M):
    bfs(point)

if min_val == N**2:
    print(-1)
else:
    print(min_val)