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


def near_process(i,j,matrix):
    same_list = []
    if j == 1:
        if matrix[i][j] == matrix[i][-1]:
            same_list.append(len(matrix[i])-1) #마지막 값 append
        if matrix[i][j] == matrix[i][j+1]:
            same_list.append(j+1) # 1보다큰 2 append
        if len(same_list) != 0 :
            same_list.append(j)
    elif j == len(matrix[i])-1 : #마지막 값일 때
        if matrix[i][j] == matrix[i][1]:
            same_list.append(1)
        if matrix[i][j] == matrix[i][j-1]:
            same_list.append(j-1)
        if len(same_list) != 0 :
            same_list.append(j)
    else: # (2 ≤ j ≤ M-1) 일 때
        if matrix[i][j] == matrix[i][j-1]:
            same_list.append(j-1)
        if matrix[i][j] == matrix[i][j+1]:
            same_list.append(j+1)
        if len(same_list) != 0 :
            same_list.append(j)
    for process in same_list:
        matrix[i][process] = 0 # x로 처리
    return matrix

def near_process2(i,j,matrix):
    same_list = []
    if i == 1:
        if matrix[i][j] == matrix[len(matrix)-1][j]:
            same_list.append(len(matrix)-1) #마지막 값 append

        if matrix[i][j] == matrix[i+1][j]:
            same_list.append(i+1) # 1보다큰 2 append

        if len(same_list) != 0 :
            same_list.append(i)

    elif i == len(matrix)-1 : #마지막 값일 때
        if matrix[i][j] == matrix[1][j]:
            same_list.append(1)

        if matrix[i][j] == matrix[i-1][j]:
            same_list.append(i-1)

        if len(same_list) != 0 :
            same_list.append(i)

    else: # (2 ≤ j ≤ M-1) 일 때
        if matrix[i][j] == matrix[i-1][j]:
            same_list.append(i-1)

        if matrix[i][j] == matrix[i+1][j]:
            same_list.append(i+1)

        if len(same_list) != 0 :
            same_list.append(i)

    for process in same_list:
        matrix[process][j] = 0 # x로 처리

    return matrix

def cal_val(matrix): #인근한 점 계산
    """
    (i, 1)은 (i, 2), (i, M)과 인접하다.
    (i, M)은 (i, M-1), (i, 1)과 인접하다.
    (i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)

    (1, j)는 (2, j)와 인접하다.
    (N, j)는 (N-1, j)와 인접하다.
    (i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)
    """
    for i in range(1,len(matrix)):
        for j in range(1, len(matrix[i])):
            re_matrix1 = near_process(i,j,matrix)
    print_list(re_matrix1)
    for i in range(1,len(matrix)):
        for j in range(1, len(matrix[i])):
            re_matrix2 = near_process2(i,j,re_matrix1)
    print_list(re_matrix2)


    return 1

N,M,T = map(int,input().split(' '))
print(N,M,T)
matrix = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    list_val = list(map(int,input().split(' ')))
    matrix[i][1:] = list_val

print_list(matrix)

for i in range(1,T+1):
    xi, di, ki = map(int,input().split(' '))
    lotation_circle(xi,di,ki,matrix)
    print_list(matrix)
    result_val = cal_val(matrix)
