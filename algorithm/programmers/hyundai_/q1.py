#반시계
def recur2(start, cnt, matrix, n, lotate):
    x,y = start[0],start[1]
    if n <= 0:
        if matrix[x][y] == 0: #다음 x,y좌표가 0(홀수면 마지막에 0이 보임)일때
            matrix[x][y] = cnt
        return
    if lotate == 0:
        for i in range(n):
            matrix[x+i][y] = cnt
            cnt += 1
        cur = [x+n-1,y+1]
    elif lotate == 1:
        for i in range(n):
            matrix[x][y+i] = cnt
            cnt += 1
        cur = [x-1,y+n-1]
    elif lotate == 2:
        for i in range(n):
            matrix[x-i][y] = cnt
            cnt += 1
        cur = [x-n+1,y-1]
    elif lotate == 3:
        for i in range(n):
            matrix[x][y-i] = cnt
            cnt += 1
        cur = [x+1,y-n+1]
    
    if lotate == 3: #시계방향 다 돌면 다시 처음방향으로
        recur2(cur, cnt, matrix, n-2, 0)
    else:
        recur2(cur, cnt, matrix, n-2, lotate+1)
        
#시계방향
def recur(start, cnt, matrix, n, lotate):
    x,y = start[0],start[1]
    if n <= 0:
        if matrix[x][y] == 0: #다음 x,y좌표가 0(홀수면 마지막에 0이 보임)일때
            matrix[x][y] = cnt
        return
    if lotate == 0:
        for i in range(n):
            matrix[x][y+i] = cnt
            cnt += 1
        cur = [x+1,y+n-1]
    elif lotate == 1:
        for i in range(n):
            matrix[x+i][y] = cnt
            cnt += 1
        cur = [x+n-1,y-1]
    elif lotate == 2:
        for i in range(n):
            matrix[x][y-i] = cnt
            cnt += 1
        cur = [x-1,y-n+1]
    elif lotate == 3:
        for i in range(n):
            matrix[x-i][y] = cnt
            cnt += 1
        cur = [x-n+1,y+1]
    
    if lotate == 3: #시계방향 다 돌면 다시 처음방향으로
        recur(cur, cnt, matrix, n-2, 0)
    else:
        recur(cur, cnt, matrix, n-2, lotate+1)
        

def solution(n, clockwise):
    if n == 1:
        return [1]
    elif n == 2:
        return [[1,1],[1,1]]
    matrix = [[0] * (n+1) for _ in range(n+1)]
    
    cnt = 1
    lotate = 0
    if clockwise: # 시계방향일때
        recur([1,1], cnt, matrix, n-1, lotate)
        recur([1,n], cnt, matrix, n-1, lotate+1)
        recur([n,n], cnt, matrix, n-1, lotate+2)
        recur([n,1], cnt, matrix, n-1, lotate+3)
    else:
        recur2([1,1], cnt, matrix, n-1, lotate)
        recur2([n,1], cnt, matrix, n-1, lotate+1)
        recur2([n,n], cnt, matrix, n-1, lotate+2)
        recur2([1,n], cnt, matrix, n-1, lotate+3)
        
    # if n % 2 != 0: #홀수 일 때
    #     val = (n //2) + 1
    #     matrix[val][val] = matrix[val][val-1] + 1
    # for i in matrix:
    #     print(i)
    result_matrix = [[0] * (n) for _ in range(n)]
    for i in range(n):
        result_matrix[i] = matrix[1+i][1:]
    
    return result_matrix


n = 6
clockwise = False
print(solution(n, clockwise))