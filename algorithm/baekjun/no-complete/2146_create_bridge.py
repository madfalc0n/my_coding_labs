def dfs(matrix,N): #dfs는 스택
    visit = []
    #시작지점탐색
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            visit.append([i,j])
            if matrix[i][j] == 1:
                start_x = i
                start_y = j
                break

    start_point = [start_x,start_y]
    stack = [start_point]
    while True:
        #육지인지 탐색
        start_x += 1
        if matrix[start_x][start_y] == 1 and [start_x,start_y] not in visit: # 탐색하려는 위치가 육지고 방문한적이 없는경우
            stack.append([start_x,start_y])
        else: #육지가 아니라면


        stack = 
        visit.append(start)







N = int(input())
matrix = [[0]*(N+1) for _ in range(N+1)] #매트릭스 생성
sum_cnt = 0
print(f"matrix")
for i in range(len(matrix)):
    print(matrix[i])
for i in range(1,N+1):
    land = list(map(int,input().split(' ')))
    matrix[i][1:] = land
print(f"input matrix")
for i in range(len(matrix)):
    sum_cnt += sum(matrix[i])
    print(matrix[i])
print(sum_cnt)
