"""
탈주범검거
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE
22:42 시작
23:10 중지
32 분 정도 썻음
23:52 시작
00:23 종료
30 분 정도 씀
대략 1시간 20분 정도
1. 시작 지하도의 입구, matrix 의 위치에서 시작
"""
def check(old, new,dir):
    # dir, 동 서 남 북
    if old == 1:
        if dir == 0 and new in [1,3,6,7]:
            return 1
        elif dir == 1 and new in [1,3,4,5]:
            return 1
        elif dir == 2 and new in [1,2,4,7]:
            return 1
        elif dir == 3 and new in [1,2,5,6]:
            return 1
    elif old == 2:
        if dir == 2 and new in [1,2,4,7]:
            return 1
        elif dir == 3 and new in [1,2,5,6]:
            return 1
    elif old == 3:
        if dir == 0 and new in [1,3,6,7]:
            return 1
        elif dir == 1 and new in [1,3,4,5]:
            return 1
    elif old == 4:
        if dir == 0 and new in [1,3,6,7]:
            return 1
        elif dir == 3 and new in [1,2,5,6]:
            return 1
    elif old == 5:
        if dir == 0 and new in [1,3,6,7]:
            return 1
        elif dir == 2 and new in [1,2,4,7]:
            return 1
    elif old == 6:
        if dir == 1 and new in [1,3,4,5]:
            return 1
        elif dir == 2 and new in [1,2,4,7]:
            return 1
    elif old == 7:
        if dir == 1 and new in [1,3,4,5]:
            return 1
        elif dir == 3 and new in [1,2,5,6]:
            return 1
    return 0

def bfs(start):
    global matrix, n, m, l

    copy_matrix = [[0] * m for _ in range(n)]

    # visit = [start]
    queue = [start]
    #동,서,남,북
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    copy_matrix[start[0]][start[1]] = 1
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            old_val = matrix[x][y]
            if nx in range(len(matrix)) and ny in range(len(matrix[0])):
                next_val = matrix[nx][ny]
                if check(old_val,next_val,i): #옮겨 갌 수 있냐?
                    if copy_matrix[nx][ny] == 0:# 한번도 온적없는 곳
                        queue.append([nx,ny])
                        copy_matrix[nx][ny] = copy_matrix[x][y] + 1
                    else: #한번 온적있다면?, 더 작으면 무시, 크면 변경
                        if copy_matrix[nx][ny] > copy_matrix[x][y] + 1:
                            copy_matrix[nx][ny] = copy_matrix[x][y] + 1
                            queue.append([nx,ny])
    # pr(copy_matrix)
    max_val = 0
    for i in range(n):
        for j in range(m):
            if 1 <= copy_matrix[i][j] <= l:
                max_val += 1
    return max_val

def pr(list):
    for i in list:
        print(i)

tc = int(input())
for case in range(1, tc+1):
    # n x m 매트릭스, 맨홀위치 (r,c), 해당지점부터 경과된 시간 l 
    n,m,r,c,l = list(map(int,input().split()))
    matrix = [ list(map(int,input().split())) for _ in range(n)]
    # pr(matrix)
    start = r,c
    result = bfs(start)
    print(f"#{case} {result}")