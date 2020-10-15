"""
연구소 바이러스 유출
https://www.acmicpc.net/problem/14502
참조 : https://pacific-ocean.tistory.com/262
"""

def bfs_virus():
    global matrix
    global result

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    queue = []
    copy = [[1] * (M+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            copy[i][j] = matrix[i][j]
            if matrix[i][j] == 2:
                queue.append([i,j])

    while queue:
        x,y = queue.pop(0)
        # print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(1,N+1) and ny in range(1,M+1):
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2
                    queue.append([nx,ny])
    tmp_cnt = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if copy[i][j] == 0:
                tmp_cnt += 1

    result = max(result,tmp_cnt)
    # print(result)


def dfs(cnt):
    global matrix

    if cnt == 3:
        bfs_virus()
    else:
        for i in range(1,N+1):
            for j in range(1,M+1):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    dfs(cnt+1)
                    matrix[i][j] = 0

N,M = list(map(int,input().split()))

matrix = [[1] * (M+1) for _ in range(N+1)]
for i in range(1,N+1):
    matrix[i] = [1] + list(map(int,input().split()))

result = 0
cnt = 0
dfs(cnt)
print(result)