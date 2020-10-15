"""
로봇청소기
https://www.acmicpc.net/problem/14503

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
 2.1 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
 2.2 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
 2.3 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
 2.4 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
청소하는 청소칸의 개수 출력

"""
def pr(list):
    for i in list:
        print(i)

def bfs(matrix, cur):
    direction = cur[2]
    # 0 북, 1 동, 2 남, 3 서
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = [[cur[0]+1, cur[1]+1]]
    
    #현재방향에서 왼쪽방향, -1이 되면 맨 마지막 인덱스로ㄱㄱ
    d_turn = direction
    while queue:
        #방향 전환한 카운트
        cnt = 0
        x,y = queue.pop(0)
        #청소했으면 2를 표시
        matrix[x][y] = 2
        for _ in range(4):
            d_turn -= 1
            if d_turn == -1:
                d_turn = 3
            nx = x + dx[d_turn]
            ny = y + dy[d_turn]
            if nx in range(1,N+1) and ny in range(1,M+1):
                if matrix[nx][ny] == 0:
                    queue.append([nx,ny])
                    break
                else:
                    cnt += 1
            else:
                cnt+= 1
        if cnt == 4:
            t_x = x + (dx[d_turn] * (-1))
            t_y = y + (dy[d_turn] * (-1))
            if t_x in range(1,N+1) and t_y in range(1,M+1):
                if matrix[t_x][t_y] == 1:
                    break
                else:
                    queue.append([t_x,t_y])
            else:
                break





N,M = list(map(int,input().split()))

# d : 0 북, 1 동, 2 남, 3 서
r,c,d = list(map(int,input().split()))
matrix = [[1] * (M+1) for i in range(N+1)]
for i in range(1,N+1):
    matrix[i] = [1] + list(map(int, input().split()))

# pr(matrix)
bfs(matrix, [r,c,d])
cnt = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if matrix[i][j] == 2:
            cnt += 1
print(cnt)
    