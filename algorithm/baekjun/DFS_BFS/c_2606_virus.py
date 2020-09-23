"""
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
"""

def bfs(start):
    visit = [start]
    queue = [start]
    while queue:
        com = queue.pop(0)
        for i in range(1,com_num+1):
            if matrix[com][i] == 1 and i not in visit: #연결되어있고 방문한적이 없는놈
                queue.append(i)
                visit.append(i)

    print(len(visit)-1)

com_num = int(input())
matrix = [[0] * (com_num+1) for _ in range(com_num+1)]
for _ in range(int(input())):
    line = list(map(int, input().split(' ')))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

# for i in range(len(matrix)):
#     print(matrix[i])

start = 1
bfs(start)