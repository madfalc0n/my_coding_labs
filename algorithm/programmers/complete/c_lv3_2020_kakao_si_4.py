"""
경주로 건설
https://programmers.co.kr/learn/courses/30/lessons/67259
도로건설 최소비용 리턴
직선도로는 100원 
코너는 500원
코너시 이전에 왔던거와 ,현재와, 그 다음거를 같이 봐야 함, 이전거와 다음거의 x,y 가 각각 증가 또는 감소 시 코너가 있는걸로 간주

x,y 둘다 차이가 발생한다면 코너(500)를 건설
x,y 중 하나만 차이가 발생한다면 직선도로(100)를 건설
"""
def bfs(start, matrix, v_matrix,s_matrix):
    v_matrix[start[0]][start[1]] = 1
    queue = [start]
    # 0 - 위, 1-아래 , 2-오른, 3-왼
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while queue:
        now_x, now_y, now_cost, now_head = queue.pop(0)
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            new_cost = now_cost + 100 if i == now_head else now_cost + 600
            if 0 < nx and nx < len(matrix) and 0 < ny and ny < len(matrix):
                if v_matrix[nx][ny] and s_matrix[nx][ny] != 0 and new_cost < s_matrix[nx][ny]:
                    s_matrix[nx][ny] = new_cost
                    queue.append([nx,ny,new_cost, i])

                if v_matrix[nx][ny] == 0 and matrix[nx][ny] == 0:
                    s_matrix[nx][ny] = new_cost
                    queue.append([nx,ny,new_cost, i]) #미래 값을 넣음
                    v_matrix[nx][ny] = 1
    
    return s_matrix[-1][-1]

def solution(board):
    n = len(board)
    price_list = list()
    matrix = [[0] * (n + 1) for _ in range(n+1)]
    v_matrix = [[0] * (n + 1) for _ in range(n+1)]
    s_matrix = [[0] * (n + 1) for _ in range(n+1)]
    for i in range(1,len(board)+1):
        matrix[i] = [0] + board[i-1] 

    # start [x,y,z,v] z = 비용 ,  v= 0 - 위 , 1 - 아래, 2- 오른쪽 , 3 왼쪽
    for j in range(1,3):
        start = [1,1,0,j]
        price_list.append(bfs(start, matrix, v_matrix,s_matrix))
        v_matrix = [[0] * (n + 1) for _ in range(n+1)]
        s_matrix = [[0] * (n + 1) for _ in range(n+1)]


    # for i in s_matrix:
    #     if sum(i) == 0:
    #         continue
    #     print(i[1:])

    print(price_list)
    return min(price_list)


#dfs...시간초과 fcuk
# price_list = []
# def check(old, now, future): #코너인지 직선인지 체크,과거,현재,미래 포인트 받아옴
#     old_x, old_y = old[0], old[1]
#     future_x, future_y = future[0], future[1]
#     if old_x == 0 and old_y == 0: #맨 초기 시작은 무조건 코너가 없다
#         return 0  
#     if abs(old_x - future_x) and abs(old_y - future_y):
#         return 1
#     else:
#         return 0

# def dfs(old, start, matrix, v_matrix, price):
#     x, y = start[0], start[1]
#     v_matrix[x][y] = 1
#     if x != 1 or y != 1:
#         price += 100
 
#     if len(price_list) != 0 and price_list[0] < price:
#         return
#     if x == len(matrix)-1 and y == len(matrix)-1:
#         price_list.insert(0,price)
#         # for i in v_matrix:
#         #     print(i)
#     else:
#         dx = [0,0,1,-1]
#         dy = [1,-1,0,0]
#         for i in range(4):
#             tmp_val = 0
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 < nx and nx < len(matrix) and 0 < ny and ny < len(matrix):
#                 if v_matrix[nx][ny] == 0 and matrix[nx][ny] == 0:
#                     if check(old, [x,y], [nx,ny]): # 코너 있으면
#                         tmp_val += 500
#                     price += tmp_val
#                     dfs([x,y], [nx,ny], matrix, v_matrix, price)
#                     price -= tmp_val
#                     v_matrix[nx][ny] = 0

# def solution(board):
#     n = len(board)
#     old = [0,0]
#     start = [1,1]
#     matrix = [[0] * (n + 1) for _ in range(n+1)]
#     v_matrix = [[0] * (n + 1) for _ in range(n+1)]
#     price = 0
#     for i in range(1,len(board)+1):
#         matrix[i] = [0] + board[i-1] 

#     dfs(old, start, matrix, v_matrix, price)
#     #print(price_list)
    
#     return price_list[0]




board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(board))
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))