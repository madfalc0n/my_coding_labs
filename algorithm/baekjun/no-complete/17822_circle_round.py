"""
원판 돌리기

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
    return matrix

def cal_val(matrix): #인근한 점 계산
    
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
    result_matrix = lotation_circle(xi,di,ki,matrix)
    print_list(matrix)
    result_val = cal_val(matrix)
