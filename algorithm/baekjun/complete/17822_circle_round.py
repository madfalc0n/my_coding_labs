"""
원판 돌리기
https://www.acmicpc.net/problem/17822
원판 반지름이 i이면 i번째 원판이라 부름
원판 하나당 M개의 정수가 적혀있다.

xi 원판 배수, 3일경우 3,6
di 시계반시계, 0이면 시계 마지막 pop 후 1번 insert, 1이면 반시계 첫 pop 후 마지막에 append
ki 몇번 회전 시킬지,
"""
def print_list(list): #출력
    for val in list:
        print(val)


def lotation_circle(xi,di,ki,matrix):#원판 회전
    len_matrix = len(matrix)
    for i in range(xi,len_matrix,xi):
        for _ in range(ki):
            if di == 0: #시계 방향 마지막 pop 후 1번 insert
                pop_val = matrix[i].pop()
                matrix[i].insert(1,pop_val)
            else: #반시계, 첫 pop 후 마지막에 append
                pop_val = matrix[i].pop(1)
                matrix[i].append(pop_val)

def bfs(start,matrix,same_result):
    x = start[0]
    y = start[1]
    ax = [0,0,1,-1]
    ay = [1,-1,0,0]
    max_len = len(matrix[0])-1
    tmp_list = []
    if y == 1:
        if matrix[x][y] == matrix[x][max_len]:
            tmp_list.append([x,max_len])
    elif y == max_len:
        if matrix[x][y] == matrix[x][1]:
            tmp_list.append([x,1])
    for i in range(4):
        nx = x + ax[i]
        ny = y + ay[i]
        if 0 < nx and nx < len(matrix) and 0 < ny and ny < len(matrix[0]):
            if matrix[x][y] == matrix[nx][ny]:
                tmp_list.append([nx,ny])

    if len(tmp_list) != 0:
        for data in tmp_list:
            if data not in same_result:
                same_result.append(data)
        if [x,y] not in same_result:
            same_result.append([x,y])
    else:
        pass

def cal_val(matrix): #인근한 점 계산
    # print("before")
    # print_list(matrix)
    same_result = []
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] != 0: #0이 아닐때 bfs 처리
                bfs([i,j],matrix,same_result)

    #bfs 통해서 인근한 점 같은 값들 리스트 전부 0으로 표시
    if len(same_result) == 0:# 인접하면서 같은 값이 없는경우 전체/값 평균
        tmp_cnt = 0
        tmp_sum = 0
        for m_list in matrix:
            tmp_sum += sum(m_list)
            tmp_cnt += len(m_list[1:]) - (m_list[1:].count(0))
        tmp_avg = tmp_sum/tmp_cnt

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] != 0:
                    if float(matrix[i][j]) < tmp_avg:
                        matrix[i][j] += 1
                    elif float(matrix[i][j]) > tmp_avg:
                        matrix[i][j] -= 1

    else:
        for data in same_result:
            matrix[data[0]][data[1]] = 0

    # print("after")
    # print_list(matrix)
    
    sum_val = 0
    for i in matrix:
        sum_val += sum(i)

    return sum_val

N,M,T = map(int,input().split(' '))
#print(N,M,T)
matrix = [[0] * (M+1) for _ in range(N+1)]
for i in range(1,N+1):
    list_val = list(map(int,input().split(' ')))
    matrix[i][1:] = list_val

# print_list(matrix)

for i in range(1,T+1):
    xi, di, ki = map(int,input().split(' '))
    lotation_circle(xi,di,ki,matrix)
    #print_list(matrix)
    result_val = cal_val(matrix)
    if result_val == 0:
        break
    

print(result_val)