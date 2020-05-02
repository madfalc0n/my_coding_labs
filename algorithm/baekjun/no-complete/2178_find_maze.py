"""
미로찾기
항상 (1,1)에서 시작해서 (N,M) 까지 이동하는 최소거리를 구함
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
DFS로 풀어야 한다.
"""
# def bfs(start,cnt):
#     distance_matrix[start[0]][start[1]] = cnt #이동거리를 여기에 저장
#     queue = [start]
#     cnt += 1
#     while queue:
#         x,y = queue.pop(0)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 < nx and nx <= N and 0 < ny and ny <= M:
#                 if matrix[nx][ny] == 1 and distance_matrix[nx][ny] == 0: #길이 있고 방문한적이없는경우
#                     distance_matrix[nx][ny] = cnt
#                     queue.append([nx,ny])
#         cnt += 1

def dfs(start,cnt):
    print(cnt)
    distance_matrix[start[0]][start[1]] = cnt
    x = start[0]
    y = start[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx and nx <= N and 0 < ny and ny <= M:
            if matrix[nx][ny] == 1 and distance_matrix[nx][ny] == 0: #길이 있고 방문한적이없는경우
                dfs([nx,ny],cnt+1)




#상하좌우
dx = [1,0,-1,0]
dy = [0,1,0,-1]
N,M = map(int,input().split(' ')) #y길이, x길이, (6,4)까지 가는데 최소거리를 구하는것
matrix = [[0] * (M+1) for _ in range(N+1)]
distance_matrix = matrix.copy()
for i in range(1,N+1):
    maze = input()
    maze = [0] + list(map(int,' '.join(maze).split(' ')))
    matrix[i] = maze

# for i in range(len(matrix)):
#     print(matrix[i])

cnt = 1
x = 1
y = 1
#bfs([x,y],cnt)
dfs([x,y],cnt)
for i in range(len(distance_matrix)):
    print(distance_matrix[i])
print(distance_matrix[N][M])