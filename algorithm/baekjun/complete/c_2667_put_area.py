""""
단지번호 붙이기
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
"""

def bfs(cur_point,cnt): #[x,y] 식으로 배열로 준다
    visit_building[cur_point[0]][cur_point[1]] = cnt
    visit = [cur_point]
    queue = [cur_point]
    while queue: #큐안에 데이터 있는경우 point에서 상하좌우로 탐색을 진행해야 함
        x,y = queue.pop(0) # x좌표,  y좌표
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx <= N and 0 <= ny and ny <= N:
                if matrix[nx][ny] == 1 and visit_building[nx][ny] == 0:
                    visit_building[nx][ny] = cnt
                    visit.append([nx,ny])
                    queue.append([nx,ny])
    #print(cnt)
    #print(visit)
    return visit


# def bfs(cur_point,cnt): #[x,y] 식으로 배열로 준다
#     visit_building[cur_point[0]][cur_point[1]] = cnt
#     visit = [cur_point]
#     queue = [cur_point]
#     while queue: #큐안에 데이터 있는경우 point에서 상하좌우로 탐색을 진행해야 함
#         x,y = queue.pop(0) # x좌표,  y좌표
#         if x>1 :#좌
#             if matrix[x-1][y] == 1 and [x-1,y] not in visit: # 현재위치에서 왼쪽에 빌딩이 있고 방문한적이 없는 경우
#                 visit_building[x-1][y] = cnt
#                 visit.append([x-1,y])
#                 queue.append([x-1,y])
#         if x<N :#우  
#             if matrix[x+1][y] == 1 and [x+1,y] not in visit: # 현재위치에서 오른쪽에 빌딩이 있고 방문한적이 없는 경우
#                 visit_building[x+1][y] = cnt
#                 visit.append([x+1,y])
#                 queue.append([x+1,y])
#         if y>1 :#상
#             if matrix[x][y-1] == 1 and [x,y-1] not in visit: # 현재위치에서 위에 빌딩이 있고 방문한적이 없는 경우
#                 visit_building[x][y-1] = cnt
#                 visit.append([x,y-1])
#                 queue.append([x,y-1])
#         if y<N :#하        
#             if matrix[x][y+1] == 1 and [x,y+1] not in visit: # 현재위치에서 아래에 빌딩이 있고 방문한적이 없는 경우
#                 visit_building[x][y+1] = cnt
#                 visit.append([x,y+1])
#                 queue.append([x,y+1])
#     return visit
        

N = int(input())
matrix = [[0] * (N+1) for _ in range(N+1)]#빈 매트릭스 생성
#상하좌우 탐색용
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(1,N+1):
    building = input()
    building = ' '.join(building)
    building = list(map(int,building.split(' ')))
    building = [0] + building
    matrix[i] = building

# for i in range(len(matrix)):
#     print(matrix[i])


visit_building = [[0] * (N+1) for _ in range(N+1)]
visit_result = []
visit_sum = []
cnt = 1
for i in range(1,N+1):
    for j in range(1,N+1):
        if matrix[i][j] == 1 and visit_building[i][j] == 0: #연결되어있고 방문하지 않았을 때
            visit_result.append(bfs([i,j],cnt)) #탐색한 좌표 저장
            cnt += 1

# print(visit_result) #탐색한 빌딩 리스트
# for i in range(len(visit_building)):
#     print(visit_building[i])

for i in range(len(visit_result)): #빌딩번호별 합 계산
    visit_sum.append(len(visit_result[i]))

print(len(visit_result))
visit_sum.sort()#오름차순 정렬
for i in range(len(visit_sum)):
    print(visit_sum[i])
