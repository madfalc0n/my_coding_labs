"""
연구소3
https://www.acmicpc.net/problem/17142
"""
from itertools import combinations
from _collections import deque
from copy import deepcopy


def check(list):
    global N
    for i in range(N):
        for j in range(N):
            if list[i][j] == '0':
                return False
    return True


def bfs(virus):
    global matrix
    global N
    global zero_cnt
    global min_time

    # copy_matrix = [[0] * N for _ in range(N)]
    copy_matrix = deepcopy(matrix)
    virus = deque(virus)
    for i,j in virus:
        copy_matrix[i][j] = 0
        
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    time = 0
    virus_cnt = 0
    while virus:
        if virus_cnt == zero_cnt:
            break
        x,y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(N) and ny in range(N):
                if copy_matrix[nx][ny] == '2':
                    virus.append((nx,ny))
                    copy_matrix[nx][ny] = copy_matrix[x][y] + 1
                    time = copy_matrix[nx][ny]
                
                elif copy_matrix[nx][ny] == '0':
                    virus.append((nx,ny))
                    copy_matrix[nx][ny] = copy_matrix[x][y] + 1
                    virus_cnt += 1    
                    time = copy_matrix[nx][ny]

        if time > min_time:
            return
    
    if check(copy_matrix):
        pass
    else:
        time = N**2

    min_time = min(min_time, time)


N, M = list(map(int,input().split()))
matrix = [input().split() for _ in range(N) ]
min_time = N**2

v_point_all = []
zero_cnt = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '2':
            v_point_all.append((i,j))
        elif matrix[i][j] == '0':
            zero_cnt += 1
# print(v_point)

for point in combinations(v_point_all,M):
    bfs(point)

if min_time == N**2:
    print(-1)
else:
    print(min_time)