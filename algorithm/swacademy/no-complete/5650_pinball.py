"""
핀볼게임
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo&categoryId=AWXRF8s6ezEDFAUo&categoryType=CODE
왔다리 갔다리
"""
def find_point(cur_point, hole_num):
    global hole_list

    x,y = cur_point[0], cur_point[1]
    if hole_list[hole_num].index([x,y]) == 0:
        return hole_list[hole_num][1]
    else:
        return hole_list[hole_num][0]


def dfs(cur, point, direction, moving_cnt):
    global matrix
    global result


    x,y = cur[0], cur[1]
    # 남,북,동,서 순
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    nx = x + dx[direction]
    ny = y + dy[direction]
    if (0 <= nx <= N+1) and (0 <= ny <= N+1):
        #벽일때, 이때까지 쌓아온 포인트 곱하기 2
        if matrix[nx][ny] == 11 or matrix[nx][ny] == 5:
            if moving_cnt != 0:
                point *= 2
                point += 1
                result = max(point,result)

        #빈공간일때 계속 ㄱㄱ
        elif matrix[nx][ny] == 0:
            dfs([nx,ny], point, direction, moving_cnt+1)

        #블랙홀일때, 이때까지 쌓아온 포인트 반환
        elif matrix[nx][ny] == -1:
            result = max(point,result)
            
        #직삼각형일때
        elif matrix[nx][ny] == 1:
            #위에서 내려 왔을떄 -> 오른쪽으로 가게
            if direction == 0:
                dfs([nx,ny], point + 1, 2, moving_cnt+1)
            #밑에서 올라 왔을떄 -> 다시 돌아가게
            elif direction == 1:
                point *= 2
                point += 1
                result = max(point,result)
                
            #왼쪽에서 왔을떄 -> 다시 돌아가게
            elif direction == 2:
                point *= 2
                point += 1
                result = max(point,result)
                    
            #오른쪽에서 왔을떄 -> 위로가게
            elif direction == 3:
                dfs([nx,ny], point + 1, 1, moving_cnt+1)


        elif matrix[nx][ny] == 2:
            #위에서 내려 왔을떄 -> 다시 돌아가게
            if direction == 0:
                point *= 2
                point += 1
                result = max(point,result)
                
            #밑에서 올라 왔을떄 -> 오른쪽으로 가게
            elif direction == 1:
                dfs([nx,ny], point + 1, 2, moving_cnt+1)
            #왼쪽에서 왔을떄 -> 다시 돌아가게
            elif direction == 2:
                point *= 2
                point += 1
                result = max(point,result)
                
            #오른쪽에서 왔을떄 -> 내려가게
            elif direction == 3:
                dfs([nx,ny], point + 1, 0, moving_cnt+1)

        elif matrix[nx][ny] == 3:
            #위에서 내려 왔을떄 -> 다시 돌아가게
            if direction == 0:
                point *= 2
                point += 1
                result = max(point,result)
                
            #밑에서 올라 왔을떄 -> 왼쪽으로 가게
            elif direction == 1:
                dfs([nx,ny], point + 1, 3, moving_cnt+1)
                
            #왼쪽에서 왔을떄 -> 내려가게
            elif direction == 2:
                dfs([nx,ny], point + 1, 0, moving_cnt+1)
            #오른쪽에서 왔을떄 -> 다시 돌아가게
            elif direction == 3:
                point *= 2
                point += 1
                result = max(point,result)
                
        
        elif matrix[nx][ny] == 4:
            #위에서 내려 왔을떄 -> 왼쪽으로 가게
            if direction == 0:
                dfs([nx,ny], point + 1, 3, moving_cnt+1)
            #밑에서 올라 왔을떄 -> 다시 돌아가게
            elif direction == 1:
                point *= 2
                point += 1
                result = max(point,result)
                
            #왼쪽에서 왔을떄 -> 다시 돌아가게
            elif direction == 2:
                dfs([nx,ny], point + 1, 1, moving_cnt+1)
            #오른쪽에서 왔을떄 -> 위로 올라가게
            elif direction == 3:
                point *= 2
                point += 1
                result = max(point,result)
                
        
        #홀일경우
        elif 6 <= matrix[nx][ny] <= 10:
            des_point = find_point([nx,ny], matrix[nx][ny])
            dfs(des_point, point, direction, moving_cnt+1)
    else:
        return



def pr(list):
    for i in list:
        print(i)

tc = int(input())
for case in range(1, tc + 1):
    N = int(input())
    result = 0
    matrix = [[11] * (N + 2) for _ in range(N+2)]
    for i in range(1, N+1):
        matrix[i] = [11] + list(map(int, input().split())) + [11]
    # pr(matrix)

    hole_list = {
        6:[],
        7:[],
        8:[],
        9:[],
        10:[],
    }
    
    start_point_list = list()
    for i in range(1,N+1):
        for j in range(1,N+1):
            if matrix[i][j] == 0:
                start_point_list.append([i,j])
            elif 6 <= matrix[i][j] <= 10:
                hole_list[matrix[i][j]].append([i,j])
            
    # print(hole_list)
    #print(start_point_list)
    #0인 곳에서 모두 시작
    for cur in start_point_list:
        point = 0
        for i in range(4):
            # print(cur)
            direction = i
            moving_cnt = 0
            dfs(cur, point, direction, moving_cnt)
    # print(start_point_list)
    # print(point_list)
    print(f"#{case} {result}")
    