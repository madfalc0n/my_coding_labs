"""
2048 이지~
https://www.acmicpc.net/problem/12100
"""
def move(matrix, dir):
    global N
    change = False

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    copy_matrix = [[0] * N for _ in range(N)]
    copy_matrix2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            copy_matrix2[i][j] = matrix[i][j]

    for i in range(N):
        for j in range(N):
            tmp_dis = 0
            nx = i
            ny = j
            while 1:
                nx += dx[dir]
                ny += dy[dir]
                if nx in range(N) and ny in range(N):
                    tmp_dis += 1
                else:
                    copy_matrix[i][j] = tmp_dis
                    break

    #똑같은 애들합치는 작업
    for i in range(N):
        for j in range(N):
            if copy_matrix[i][j] == 0:
                ox, oy = i, j
                nx, ny = i, j
                while ox in range(N) and oy in range(N):
                    if copy_matrix2[ox][oy] != 0:
                        nx, ny = ox + (dx[dir] * (-1)), oy + (dy[dir] * (-1))
                        while nx in range(N) and ny in range(N):
                            if copy_matrix2[ox][oy] == copy_matrix2[nx][ny]:
                                copy_matrix2[ox][oy] *= 2
                                copy_matrix2[nx][ny] = 0
                                change = True
                                break
                            elif copy_matrix2[nx][ny] != 0 and copy_matrix2[ox][oy] != copy_matrix2[nx][ny]:
                                break
                            elif copy_matrix2[nx][ny] == 0:
                                nx += (dx[dir] * (-1))
                                ny += (dy[dir] * (-1)) 
                    ox += (dx[dir] * (-1))
                    oy += (dy[dir] * (-1)) 


    #합치고나서 0 된 애들을 찾아서 루프 돌려
    for i in range(N):
        for j in range(N):
            if copy_matrix[i][j] == 0:
                ox, oy = i, j
                
                while ox in range(N) and oy in range(N):
                    if copy_matrix2[ox][oy] == 0:
                        nx, ny = ox,oy
                        while nx in range(N) and ny in range(N):
                            if copy_matrix2[nx][ny] != 0:
                                copy_matrix2[ox][oy], copy_matrix2[nx][ny] = copy_matrix2[nx][ny], copy_matrix2[ox][oy]
                                change = True
                                break
                            nx += (dx[dir] * (-1))
                            ny += (dy[dir] * (-1)) 
                    ox += (dx[dir] * (-1))
                    oy += (dy[dir] * (-1)) 

    return [copy_matrix2,change]

def dfs(matrix, cost):
    global result
    if cost == 5:
        for i in range(N):
            for j in range(N):
                result = max(matrix[i][j], result)
    else:
        for i in range(4):
            tmp_matrix, change = move(matrix, i)
            if change:
                dfs(tmp_matrix, cost + 1)
            
N = int(input())
matrix = [[0] * (N) for _ in range(N)]
for i in range(N):
    matrix[i] = list(map(int, input().split()))

result = 0
cost = 0
if N == 1:
    print(matrix[0][0])
else:
    dfs(matrix, cost)
    print(result)

