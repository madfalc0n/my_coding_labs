"""
주사위 굴리기
https://www.acmicpc.net/problem/14499
17:30 시작
18:32 종료
"""
def move(dir):
    global dice
    
    #1 동, 2 서, 3 남, 4 북
    if dir == 1:
        tmp_val = dice[1].pop(-1)
        tmp_under = dice[3][1]
        dice[3][1] = tmp_val
        dice[1].insert(0,tmp_under)

    elif dir == 2:
        tmp_val = dice[1].pop(0)
        tmp_under = dice[3][1]
        dice[3][1] = tmp_val
        dice[1].append(tmp_under)        
    elif dir == 3:
        val1,val2,val3,val4 = dice[0][1],dice[1][1],dice[2][1],dice[3][1]
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = val2, val3, val4, val1
    elif dir == 4:
        val1,val2,val3,val4 = dice[0][1],dice[1][1],dice[2][1],dice[3][1]
        dice[0][1],dice[1][1],dice[2][1],dice[3][1] = val4, val1, val2, val3


dice = [[0] * 3 for _ in range(4)]
N,M,x,y,k = list(map(int,input().split()))
matrix = [ list(map(int,input().split())) for _ in range(N) ]
command = list(map(int,input().split()))
# print(N,M,x,y,k)
# print(matrix)
# print(command)
# print(dice)

#1 동, 2 서, 3 북, 4 남
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

nx = x
ny = y

for com in command:
    tmp_x = nx
    tmp_y = ny
    nx += dx[com]
    ny += dy[com]
    if nx in range(N) and ny in range(M):
        move(com)
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = dice[3][1]
        else:
            dice[3][1] = matrix[nx][ny]
            matrix[nx][ny] = 0
        print(dice[1][1]) 
    else:
        nx = tmp_x
        ny = tmp_y