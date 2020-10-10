"""
프로세서 연결하기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf

최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이의 합을 구하고자 한다.
전원에 연결되지 못하는 core도 있을 수 있따.
단, 여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값을 구하라.

"""
def dfs(cur_core, connect_core_cnt, cost):
    global N
    global matrix
    global check_core_list_2
    global result
    global full_cost_list
    global nor_cost_list

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    #모든 코어 정복 했으면?
    if cur_core == len(check_core_list_2):
        if cur_core == connect_core_cnt:
            full_cost_list.add(cost)
        elif cur_core > connect_core_cnt:
            nor_cost_list.add(cost)
    else:
        #현재 코어의 x,y 좌표
        x,y = check_core_list_2[cur_core][0], check_core_list_2[cur_core][1]
        # 동 0 서 1 남 2 북 3
        for i in range(4):
            tmp_cnt = 0
            nx = x
            ny = y
            while 1:
                nx += dx[i]
                ny += dy[i]

                if 1 <= nx <= N and 1 <= ny <= N:
                    #전선 연결할 길이있으면
                    if matrix[nx][ny] == 0:
                        matrix[nx][ny] = 2
                        tmp_cnt += 1
                    else:
                        while tmp_cnt > 0:
                            nx -= dx[i]
                            ny -= dy[i]
                            matrix[nx][ny] = 0
                            tmp_cnt -= 1
                        break
                else:
                    break

            if tmp_cnt != 0:
                dfs(cur_core + 1, connect_core_cnt + 1, cost + tmp_cnt)
                #백트래킹 통해서 다시 초기화
                while tmp_cnt > 0:
                    nx -= dx[i]
                    ny -= dy[i]
                    matrix[nx][ny] = 0
                    tmp_cnt -= 1



#전원연결할수 있는 라인개수 체크
def check_line(matrix, core, N):
    update_core_list = []
    for i in core:
        x,y,c_p = i[0] , i[1], i[2]
        # print(x,y,c_p)
        
        # 동
        nx, ny = x, y
        while 1:
            ny += 1
            if matrix[nx][ny] != 0:
                break
            if (nx == 1 or nx == N) or (ny == 1 or ny == N):
                c_p += 1
                break
        
        # 서
        nx, ny = x, y
        while 1:
            ny -= 1
            if matrix[nx][ny] != 0:
                break
            if (nx == 1 or nx == N) or (ny == 1 or ny == N):
                c_p += 1
                break

        # 남
        nx, ny = x, y
        while 1:
            nx += 1
            if matrix[nx][ny] != 0:
                break
            if (nx == 1 or nx == N) or (ny == 1 or ny == N):
                c_p += 1
                break

        # 북
        nx, ny = x, y
        while 1:
            nx -= 1
            if matrix[nx][ny] != 0:
                break
            if (nx == 1 or nx == N) or (ny == 1 or ny == N):
                c_p += 1
                break
        if c_p != 0:
            update_core_list.append((x,y,c_p))
    return update_core_list

def pr(list):
    for i in list:
        print(i)


#메인 부분
total_tc  = int(input())
for start in range(1, total_tc+1):
    N = int(input())
    matrix = [ [-1] * (N+1) for _ in range(N+1) ]
    for i in range(1, N+1):
        matrix[i] = [-1] + list(map(int, input().split(' ')))
    # pr(matrix)
    total_core_list = []
    check_core_list = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] == 1:
                total_core_list.append([i,j])
                if (1 < i < N) and (1 < j < N):
                    check_core_list.append([i,j,0])
    check_core_list_2 = check_line(matrix, check_core_list, N)
    check_core_list_2 = sorted(check_core_list_2, key= lambda x: x[2])
    # print(check_core_list_2)
    connect_core_cnt = 0
    cur_core = 0
    cost = 0
    result = 10000
    full_cost_list = set()
    nor_cost_list = set()
    dfs(cur_core, connect_core_cnt, cost)

    print(f"#{start} {min(full_cost_list)}")
    # print(nor_cost_list)