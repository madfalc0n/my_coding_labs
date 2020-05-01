""""
단지번호 붙이기
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
"""
def bfs(cur_point):
    visit = [cur_point]
    queue = [cur_point]
    while queue:
        point = queue.pop(0)
        for i in range(start,N+1):
            if 1 < start and start < N+1: #매트릭스 안에 있을 때

            if matrix[start][i] == 1 and [start,i] not in visit:






N = int(input())
matrix = [[0] * (N+1) for _ in range(N+1)]#빈 매트릭스 생성
visit_building = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    building = input()
    building = ' '.join(building)
    building = list(map(int,building.split(' ')))
    building = [0] + building
    matrix[i] = building

for i in range(len(matrix)):
    print(matrix[i])


for i in range(1,N+1):
    for j in range(1,N+1):
        if matrix[i][j] == 1 and visit_building[i][j] == 0: #연결되어있고 방문하지 않았을 때
            bfs(i,j)