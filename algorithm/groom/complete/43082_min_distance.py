"""
최단 거리 구하기
https://level.goorm.io/exam/43082/%EC%B5%9C%EB%8B%A8-%EA%B1%B0%EB%A6%AC-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1
"""


def pr(m):
    for i in m:
        print(i)

def bfs(start):
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    visit = [start]
    queue = [start]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if [nx,ny] not in visit and 0 < nx <= n and 0 < ny <= n:
                # print(nx,ny)
                if m[nx][ny] == 1:
                    m[nx][ny] = m[x][y] + 1
                    visit.append([nx,ny])
                    queue.append([nx,ny])
                

n = int(input())
m = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
	m[i] = [0] + list(map(int, input().split(' ')))

start = [1,1]
bfs(start)
# pr(m)
print(m[n][n])