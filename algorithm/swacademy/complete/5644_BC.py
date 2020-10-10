"""
무선충전
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&categoryId=AWXRDL1aeugDFAUo&categoryType=CODE
전체크기는 10x10 고정
"""


# def make_bc2(matrix, point, num):
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     x,y = point[0],point[1]
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx in range(1,11) and ny in range(1,11):
#             if matrix[nx][ny] == '0':
#                 matrix[nx][ny] = str(num)
#             elif str(num) not in matrix[nx][ny] and matrix[nx][ny] != '0':
#                 matrix[nx][ny] += str(num)

# def make_bc(matrix, point, num, c):
#     dx = [0,0,1,-1]
#     dy = [1,-1,0,0]
#     x,y = point[0],point[1]
#     if matrix[x][y] != '0':
#         matrix[x][y] += str(num)
#     else:
#         matrix[x][y] = str(num)
#     queue = [[x,y]]
#     visit = [[x,y]]
#     for i in range(4):
#         cnt = c
#         nx = x
#         ny = y
#         while cnt > 1:
#             nx += dx[i]
#             ny += dy[i]
#             if nx in range(1,11) and ny in range(1,11):
#                 if matrix[nx][ny] == '0' :
#                     matrix[nx][ny] = str(num)
#                 elif str(num) not in matrix[nx][ny] and matrix[nx][ny] != '0':
#                     matrix[nx][ny] = str(num)
#                 visit.append([nx,ny])
#                 if cnt != 1:

#             cnt -= 1




#     # while queue:
#     #     x,y = queue.pop(0)
#     #     if cnt > 0:
#     #         for i in range(4):
#     #             nx = x + dx[i]
#     #             ny = y + dy[i]
#     #             if [nx,ny] not in visit and nx in range(1,11) and ny in range(1,11):
                    
#     #                 if matrix[nx][ny] != '0':
#     #                     matrix[nx][ny] += str(num)
#     #                 else:
#     #                     matrix[nx][ny] = str(num)    
#     #                 queue.append([nx,ny])
#     #                 visit.append([nx,ny])
#     #     cnt -= 1

def cal_score(a,b):
    score = 0

    if len(a) == 0 and len(b) == 0:
        return score

    elif len(a) == 0 and len(b) != 0:
        for key in b:
            score = max(score,ap_list[key][3])
    elif len(a) != 0 and len(b) == 0:
        for key in a:
            score = max(score,ap_list[key][3])

    else:
        for a_key in a:
            for b_key in b:
                if a_key == b_key:
                    score = max(score,ap_list[a_key][3])
                else:
                    score = max(score,ap_list[a_key][3]+ap_list[b_key][3])
    
    return score


def cal_dis(point):
    global ap_list
    # key : [x, y, c, p]
    x, y = point[0], point[1]
    p_list = []
    for key in ap_list.keys():
        distance = abs(x-ap_list[key][0]) + abs(y-ap_list[key][1])
        if ap_list[key][2] >= distance:
            p_list.append(key)
    return p_list


def proc(start,user_move,time):
    #이동없음, 상, 우, 하, 좌
    dx = [0,-1,0,1,0]
    dy = [0,0,1,0,-1]
    x,y = start[0], start[1]
    user_ap_list = []

    for i in range(time):
        move = user_move[i]
        x += dx[move]
        y += dy[move]
        p_ap_list = cal_dis([x,y])

        user_ap_list.append(p_ap_list)

    return user_ap_list


def pr(list):
    for i in list:
        print(i)

tc = int(input())

for case in range(1,tc+1):
    matrix = [['0'] * 11 for _ in range(11)]
    
    time, bc_num = list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    
    ap_list = dict()
    for i in range(1,bc_num+1):
        y,x,c,p = list(map(int,input().split()))
        ap_list[i] = [x,y,c,p]
    user_a = proc([1,1],a,time+1)
    # print(user_a)
    user_b = proc([10,10],b,time+1)
    # print(user_b)
    
    result = 0
    for i in range(time+1):
        result += cal_score(user_a[i], user_b[i])

    print(f"#{case} {result}")