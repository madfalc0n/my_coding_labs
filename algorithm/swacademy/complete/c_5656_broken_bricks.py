"""
벽돌깨기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&categoryId=AWXRQm6qfL0DFAUo&categoryType=CODE
16:00 시작

1. 값이 0이 아닌 애들의 좌표를 찾는다.
"""

def clean_zero(matrix):
    global h,w

    for i in range(w):
        tmp_list = []
        tmp_cnt = 0
        for j in range(h):
            if matrix[j][i] != 0:
                tmp_list.append(matrix[j][i])
            else:
                tmp_cnt += 1
        tmp_list = ([0] * tmp_cnt) + tmp_list
        for x in range(h):
            matrix[x][i]  = tmp_list[x]
    

#벽돌 제거
def remove_bricks(matrix, start):
    global h,w
    copy_matrix = [[0] * w for _ in range(h)]
    for i in range(w):
        for j in range(h):
            copy_matrix[j][i] = matrix[j][i]

    x,y = start
    # if start == [2,2]:
    #     print(0)
    queue = [start]
    visit = [start]
    dx,dy = [1,-1,0,0],[0,0,-1,1]
    while queue:
        x,y = queue.pop(0)
        if copy_matrix[x][y] <= 1: # 해당 블록 값이 1보다 작으면 0으로 바꾸고 종료
            copy_matrix[x][y] = 0
            continue
        else:
            val = copy_matrix[x][y]
            for i in range(4):
                nx = x
                ny = y
                for _ in range(val-1):
                    nx += dx[i]
                    ny += dy[i]
                    if nx in range(h) and ny in range(w):
                        if [nx,ny] not in visit:
                            visit.append([nx,ny])
                            queue.append([nx,ny])
            copy_matrix[x][y] = 0

    clean_zero(copy_matrix)
    
    return copy_matrix

def dfs(matrix, start_list,cost):
    global n, result

    if start_list.count(None) == len(start_list):
        result = 0
    else:
        #모든 구슬 다 쓸경우
        if cost == n:
            tmp_cnt = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != 0:
                        tmp_cnt += 1
            result = min(result,tmp_cnt)
        else:
            for i in range(len(start_list)):
                tmp_point = start_list[i]
                if tmp_point == None:
                    continue
                remove_result = remove_bricks(matrix, tmp_point)
                update_start_list = find_start_point(remove_result)
                dfs(remove_result, update_start_list, cost+1)
            
            


#시작점 찾기
def find_start_point(matrix):
    global h,w
    point_list = [None] * w
    # print(point_list)
    for i in range(w): # 세로
        for j in range(h): # 가로
            if matrix[j][i] != 0: # 0,0 1,0 2,0 3,0 4,0 ~~~ x,0
                # print(j,i)
                point_list[i] = [j,i]
                break 
    return point_list



def pr(list):
    for i in list:
        print(i)

tc = int(input())
for case in range(1,tc+1):
    n,w,h = list(map(int,input().split()))
    matrix = [list(map(int,input().split())) for _ in range(h)]
    # pr(matrix)
    
    start_list = find_start_point(matrix)
    # print(start_list)
    cost = 0
    result = w*h
    dfs(matrix, start_list,cost)
    print(f"#{case} {result}")