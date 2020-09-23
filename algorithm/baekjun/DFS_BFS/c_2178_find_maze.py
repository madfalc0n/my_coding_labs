"""
https://www.acmicpc.net/problem/2178
미로찾기
항상 (1,1)에서 시작해서 (N,M) 까지 이동하는 최소거리를 구함
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
BFS로 풀어야 한다.
"""

def bfs(start, end, visit, matrix):
    cnt = 1
    tx,ty = start
    visit[tx][ty] = cnt
    queue = [[tx,ty]]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x,y = queue.pop(0)
        cnt = visit[x][y] + 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx,ny,end[0],end[1])
            if 0 < nx <= end[0] and 0 < ny <= end[1] and visit[nx][ny] == 0 and matrix[nx][ny] == 1:
                    visit[nx][ny] += cnt
                    queue.append([nx,ny])  

    

N,M = list(map(int, input().split()))
# print(N,M)
matrix = [[0] * (M+1) for _ in range(N+1)]
visit = [[0] * (M+1) for _ in range(N+1)]
for i in range(1,N+1):
    matrix[i] = [0] + list(map(int,input()))
# for i in matrix:
#     print(i)


start = [1,1]
end = [N,M]
bfs(start, end, visit, matrix)

print(visit[N][M])







# def tmp_print(list):
#     for i in list:
#         for j in i:
#             print(j,end='   ')
#         print()

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
# def bfs(start,cnt):
#     cpy_matrix[start[0]][start[1]] = cnt
#     queue = [start]
#     while queue:
#         x,y = queue.pop(0)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 < nx and nx <= N and 0 < ny and ny <= M:
#                 if matrix[nx][ny] == 1 and cpy_matrix[nx][ny] == 0:
#                     cpy_matrix[nx][ny] = cpy_matrix[x][y] +1
#                     queue.append([nx,ny])

# N,M = map(int,input().split(' ')) # N은 x축, M은 y축
# matrix = [[0] * (M+1) for _ in range(N+1)]
# cpy_matrix = matrix.copy()
# for i in range(1,len(matrix)):
#     m_list = list(input())
#     matrix[i] = [0] + list(map(int,m_list))

# #입력값 출력
# #tmp_print(matrix)

# #탐색시작
# start = [1,1]
# cpy_matrix[1][1] = 1
# cnt = 1
# #dfs(start,cnt)
# bfs(start,cnt)
# tmp_print(cpy_matrix)
# print(cpy_matrix[N][M])
