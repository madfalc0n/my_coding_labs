"""

도로건설 최소비용 리턴
직선도로는 100원 
코너는 500원
코너시 이전에 왔던거와 ,현재와, 그 다음거를 같이 봐야 함, 이전거와 다음거의 x,y 가 각각 증가 또는 감소 시 코너가 있는걸로 간주

"""
global_visit_list = []
def dfs(matrix,start,visit): #재귀 이용
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    #result_list.append(start)
    #print(result_list)
    x = start[0]
    y = start[1]
    visit.append([x,y])
    if x == len(matrix)-1 and y == len(matrix)-1: #정점에 도달했을 때        
        return global_visit_list.append(visit)
    print(f"visit__list : {visit}")
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < len(matrix) and 0 <= ny and ny < len(matrix): # 매트릭스 범위안에 들어갈 때
            if matrix[nx][ny] == 0 and [nx,ny] not in visit:#벽이 아니고 방문한 적 없을 때
                dfs(matrix,[nx,ny],visit)
                #global_visit_list.append(re)
                visit.pop()


def solution(board):
    len_board =len(board)
    matrix = board
    visit = []
    for i in visit:
        print(i)
    start = [0,0]
    total_list = dfs(matrix,start,visit)
    print(total_list)
    print('glo')
    print(global_visit_list)
    answer = 0
    return answer

board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))