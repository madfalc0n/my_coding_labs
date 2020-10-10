"""
등산로
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE
"""

def dfs(start, cost, cur_val, visit, chance):
    global N
    global result
    global K
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    x,y = start[0], start[1]
    # if x == 3 and y == 5:
    #     testb = 0
    #     dsf = 0
    #     print(x,y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if [nx,ny] not in visit and nx in range(1,N+1) and ny in range(1,N+1):
            if matrix[nx][ny] < cur_val:
                visit.append([nx,ny])
                result = max(result, cost + 1)
                dfs([nx,ny], cost+1, matrix[nx][ny], visit, chance)
                visit.pop(-1)

            if chance == True:
                for dec in range(1,K+1):
                    matrix[nx][ny] -= dec
                    if matrix[nx][ny] < cur_val:
                        visit.append([nx,ny])
                        result = max(result, cost + 1)
                        dfs([nx,ny], cost+1, matrix[nx][ny], visit, False)
                        chance = True
                        visit.pop(-1)
                    matrix[nx][ny] += dec
            

def pr(list):
    for i in list:
        print(i)

tc = int(input())
for case in range(1, tc+1):
    result = 0
    chance = True
    N, K = list(map(int,input().split()))
    matrix = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1,N+1):
        matrix[i] = [0] + list(map(int,input().split()))
    
    val_dict = dict()
    max_index = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            val_dict[matrix[i][j]] = val_dict.get(matrix[i][j],[]) + [[i,j]]

    max_index = max(val_dict.keys())
    # print(val_dict)
    # dict_list = [0] + sorted(val_dict.items(),key= lambda x: x[0])
    # print(dict_list)
    # dict_list[9][1].pop(0)
    # print(dict_list)
    cost = 1
    visit = []
    for point in val_dict[max_index]:
        visit = [[point[0],point[1]]]
        cur_val = matrix[point[0]][point[1]]
        dfs(point, cost, cur_val, visit, chance)

    print(f"#{case} {result}")
