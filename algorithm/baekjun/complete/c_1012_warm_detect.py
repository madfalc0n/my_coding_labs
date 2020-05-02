"""
유기농 배추
해충을 잡아먹는 배추흰지렁이의 마리수 찾기
백준의 2667번 문제와 유사한것으로 보인다.

입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
M(1 ≤ M ≤ 50)
N(1 ≤ N ≤ 50)
K(1 ≤ K ≤ 2500)
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
"""
def bfs(start,cnt):
    visit_cabbage = [start]
    matrix_cnt[start[0]][start[1]] = cnt
    queue = [start]
    while queue:
        x,y = queue.pop(0)
        #상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if matrix[nx][ny] == 1 and [nx,ny] not in visit_cabbage: # 해당영역에 지렁이 있고 방문한적이 없는경우
                    matrix_cnt[nx][ny] = cnt
                    queue.append([nx,ny])
                    visit_cabbage.append([nx,ny])

    return visit_cabbage
            



#상하좌우 탐지용
dx = [0,0,1,-1]
dy = [1,-1,0,0]
test_case = int(input())
save_cnt = []   
for _ in range(test_case):
    visit_cabbage = []
    M,N,K = map(int,input().split(' ')) #가로길이, 세로길이, 배추의 위치
    
    # #가로세로배추위치 값조회
    # print(M,N,K)
    
    matrix = [[0] * (M) for _ in range(N) ] #영역 생성
    matrix_cnt = matrix.copy() #지역별 마리수 카운트
    # #생성된영역 조회
    # for j in range(len(matrix)):
    #     print(matrix[j])
    
    #배추지정
    for _ in range(K):
        x,y = map(int,input().split(' '))
        matrix[y][x] = 1
    
    # #배추 조회
    # for i in range(len(matrix)):
    #     print(matrix[i])

    #완탐시작
    cnt = 0 #지렁이 마리수 저장할 공간
    

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and [i,j] not in visit_cabbage: #배추가 있고 방문한 적이 없는 경우
                cnt += 1
                visit_cabbage.extend(bfs([i,j],cnt))
                #print(visit_cabbage)
    
    #지렁이 수 출력
    save_cnt.append(cnt)

for i in save_cnt:
    print(i)
