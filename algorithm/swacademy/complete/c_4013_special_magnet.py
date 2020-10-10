"""
특이한 자석
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH&categoryId=AWIeV9sKkcoDFAVH&categoryType=CODE
"""

    

#현재 매트릭스에서 서로 다른 자성을 가진놈들 판별(bfs)
def check_move_list(matrix, move_index):
    tmp_matrix = [[0] * 4 for _ in range(4)]
    visit = []
    queue = []

    for i in range(3):
        if matrix[i][2] != matrix[i+1][6]:
            tmp_matrix[i][i+1] = 1
            tmp_matrix[i+1][i] = 1

    queue = [move_index]
    visit = [move_index]
    while queue:
        cur = queue.pop(0)
        for i in range(len(tmp_matrix[cur])):
            if i not in visit and tmp_matrix[cur][i] == 1:
                visit.append(i)
                queue.append(i)

    return sorted(visit)

#실제 톱티바퀴 움직이기 위한 함수
def move_matrix(matrix, move_index, direction):
    #시계방향은 1 반시계는 -1
    if direction == 1:
        tmp_val = matrix[move_index].pop(-1)
        matrix[move_index].insert(0, tmp_val)
    else:
        tmp_val = matrix[move_index].pop(0)
        matrix[move_index].append(tmp_val)

def move_manage(matrix, move_index, direction):
    move_list = check_move_list(matrix, move_index)
    # print(move_list)

    
    #맨 처음 인덱스가 짝수이면? 
    if move_index % 2 == 0:
        dot = False
    else:
        dot = True

    for index in move_list:
        #첫 인덱스가 짝수일 때
        if dot == False:
            if index % 2 == 0:
                #방향은 그대로
                move_matrix(matrix, index, direction)
            else:
                #홀수면 방향은 반대로
                move_matrix(matrix, index, direction * (-1))
        else:
            if index % 2 == 0:
                #방향은 반대로
                move_matrix(matrix, index, direction * (-1))
            else:
                #방향은 그대로
                move_matrix(matrix, index, direction)
    # pr(matrix)
    
def pr(list):
    for i in list:
        print(i)

tc = int(input())
for case in range(1, tc+1):
    change_chance = int(input())
    matrix = [[0] * 8 for _ in range(4)] 

    for i in range(4):
        matrix[i] = list(map(int,input().split()))
    # pr(matrix)

    #특정 톱니, 시계 or 반시계
    for i in range(change_chance):
        #움직일 톱니바퀴 번호와 움직일 방향 인덱스번호랑 맞추기위해 -1 처리
        move_index, direction = list(map(int, input().split()))
        move_index -= 1
        move_manage(matrix, move_index, direction)
    
    # print("result")
    # pr(matrix)
    result = 0
    for i in range(4):
        if matrix[i][0] == 1:
            result += (2**i)
    print(f"#{case} {result}")