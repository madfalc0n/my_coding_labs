""""
단지번호 붙이기
https://www.acmicpc.net/problem/2667
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
"""
def pr(list):
    print(len(list))
    for i in list:
        print(i)

def bfs(start, building_num):
    x, y = start[0], start[1]
    v_matrix[x][y] = building_num
    matrix[x][y]  = building_num
    queue = [start]
    cnt = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx and nx <= num and 0 < ny and ny <= num:
                if matrix[nx][ny] != 0 and v_matrix[nx][ny] == 0:
                    queue.append([nx,ny])
                    v_matrix[nx][ny] = 1
                    matrix[nx][ny] = building_num
                    cnt += 1
    return cnt

num = int(input())
matrix = [[0] * (num + 1) for _ in range(num+1)]
v_matrix = [[0] * (num + 1) for _ in range(num+1)]

for i in range(1,num+1):
    matrix[i] = [0] + list(map(int,list(input())))

visit_cnt = list()
building_num = 1
for i in range(1,num+1):
    for j in range(1,num+1):
        if v_matrix[i][j] == 0 and matrix[i][j] == 1: #방문한 적이 없고, 빌딩이 있을 때 탐색
            tmp_val = bfs([i,j],building_num)
            building_num += 1
            visit_cnt.append(tmp_val)

#pr(matrix)
visit_cnt = sorted(visit_cnt)
pr(visit_cnt)