"""
백준 연구소
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 
0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다.(벽을 제외하고 바이러스로 채워진다.)
2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
결국 빈칸에 바이러스를 채우라는 이야기이다.
1.바이러스 위치를 파악하고 동시에 퍼뜨릴수 있는 바이러스 매칭 구함
2.바이러스 쌍별로 탐색(bfs 시작)
3.탐색 완료 후 시간초 확인, 먼저 빈공간 있는지 파악(-1 반환), 없으면 최대 시간 반환
"""
from itertools import combinations

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(start):
    cnt = 1
    time_matrix[start[0]][start[1]] = 0 #현재지점 0으로 지정
    visit = [start]
    queue = [start]
    tmp_que = []
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx and nx <= N and 0 < ny and ny <= N:
                if matrix[nx][ny] == 0 and [nx,ny] not in visit:
                    visit.append([nx,ny])
                    time_matrix[nx][ny] = time_matrix[x][y] + 1
                    queue.append([nx,ny])
    tmp_print(time_matrix)




def tmp_print(matrix):
    print(f"insert matrix")
    for i in matrix:
        for j in i:
            print(j,end='      ')
        print()
    print("end")








N,M = map(int,input().split(' ')) #N 크기, M 동시바이러스 퍼뜨리기 수
matrix = [['?'] * (N+1) for _ in range(N+1)]
time_matrix = matrix.copy()
virus_location = []
for i in range(1,N+1):
    tmp_list = ['?'] + list(map(int,input().split(' ')))
    matrix[i] = tmp_list

    #바이러스, 벽, 빈공간 을 새로표시
    for x in range(1,len(matrix[i])):
        if matrix[i][x] == 2 : #바이러스일 때, 위치도 표시해줌
            time_matrix[i][x] = '*'
            virus_location.append([i,x])
        elif matrix[i][x] == 1 : # 벽일떄
            time_matrix[i][x] = '#'
        else: #빈공간일떄
            time_matrix[i][x] = '-1'

tmp_time_matrix = time_matrix.copy()
#tmp_print(matrix)
#tmp_print(time_matrix)


#바이러스 동시에 퍼뜨릴수 있는 개수만큼 묶어버리기
#print(virus_location)
virus_location = list(combinations(virus_location,M))
#print(virus_location)


result = []
for virus in virus_location:
    for v_l in virus:
        bfs(v_l)
    #tmp_print(time_matrix)
    max_v = 0
    for find_max in time_matrix:
        #print(find_max)
        for val in find_max: #리스트
            if type(val) == int:
                if val == -1: #-1 경우
                    max_v = -1
                    break
                else: #없을경우 맥스값
                    if max_v < val:
                        max_v = val
    result.append(max_v)
    time_matrix = tmp_time_matrix


print(result)
if result.count(-1):
    print(-1)
else:
    print(min(result))
























# from itertools import combinations
#
#
#
# def bfs(start):
#     cnt = 0
#     visit_matrix = time_matrix.copy()
#     time_matrix[start[0]][start[1]] = cnt
#     queue = [start]
#     while queue:
#         cnt += 1
#         x,y = queue.pop(0)
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 < nx and nx < N and 0 < ny and ny < N:
#                 if matrix[nx][ny] == 0 and time_matrix[nx][ny] != '-' and time_matrix[nx][ny] != '*':#빈칸이고 방문하지 않았을떄(-1일떄)
#                         visit_matrix[nx][ny] =
#                          time_matrix[nx][ny] = cnt
#                          queue.append([nx,ny])
#     # for i in range(len(time_matrix)):
#     #         print(time_matrix[i])
#
#
#
#
# N,M = map(int,input().split(' ')) # N은 연구소크기, M은 바이러스 개수
# matrix = [[0] * (N+1) for _ in range(N+1)]
# time_matrix = [[0] * (N+1) for _ in range(N+1)]
# virus_location = []
# for i in range(1,N+1):
#     lab_list = [0]+list(map(int,input().split(' ')))
#     for tmp_index, data in enumerate(lab_list):
#         if data == 2:#바이러스일때
#             virus_location.append([i,tmp_index])
#             time_matrix[i][tmp_index] = '*'
#         if data == 0 and tmp_index > 0:#빈칸일때
#             time_matrix[i][tmp_index] = -1
#         if data == 1:
#             time_matrix[i][tmp_index] = '-'
#
#     matrix[i] = lab_list
#
# print(f"매트릭스 정보")
# for i in range(len(matrix)):
#     print(matrix[i])
# print()
#
# print(f"타임 매트릭스 정보")
# for i in range(len(matrix)):
#     print(time_matrix[i])
# print()
#
#
# #바이러스 위치 확인
# print("virus_location")
# print(virus_location)
#
# #동시에 바이러스 퍼뜨릴 수 있는 거 매칭
# #print("virus_match")
# virus_permute = list(combinations(virus_location,M))
# print(virus_permute)
# #virus_permute[0] 식으로 쌍을 호출할 수 있음
#
#
# #2. 바이러스 쌍별로 탐색
# #상하좌우 탐색용
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# # print('time_matrix')
# # for i in range(len(time_matrix)):
# #     print(time_matrix[i])
#
# cpy_time_matrix = time_matrix.copy()
# #print("탐색시작")
# visit_result = []
# max_v = []
# min_v = []
# for i in virus_permute:
#     for j in i:#동시에 가능한만큼
#         bfs(j)
#     print("변형")
#     for x in range(len(time_matrix)):
#         print(time_matrix[x])
#     print("end")
#
#     for x in time_matrix: #bfs 돌리고 난 후 -1 있는지 검사
#         temp = 0
#         for xx in x:
#             if xx != '-' and xx != '*' and xx != -1:
#                 mx_tmp = max(xx,temp)
#                 visit_result.append(mx_tmp)
#             elif xx == -1:
#                 visit_result.append(-1)
#     time_matrix = cpy_time_matrix
#     if visit_result.count(-1) == 0: #-1 없을경우 전부 퍼뜨림
#         max_v.append(max(visit_result))
#     else:
#         min_v.append(-1)
#     visit_result = []
# if len(virus_permute) == len(min_v):
#     print(-1)
# else:
#     print(min(max_v))