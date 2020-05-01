# def dfs(matrix,N): #dfs는 스택
#     #시작지점탐색
#     for i in range(1,len(matrix)):
#         for j in range(1,len(matrix[i])):
#             if matrix[i][j] == 1:
#                 start_x = i
#                 start_y = j
#     visit = []
#     stack = []
#     while True:
#         #육지인지 탐색
#         if matrix[start[0]][start[1]] == 1:
        
#         else: #육지가 아니라면


#         stack = 
#         visit.append(start)







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
