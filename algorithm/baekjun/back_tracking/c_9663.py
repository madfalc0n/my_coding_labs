"""
백트래킹
N-Queen
https://www.acmicpc.net/problem/9663
시간 초과로 인한 pypy3 로 제출
"""

def chk_line(row,col,matrix):
    if sum([matrix[row][i] for i in range(N)]) >= 1 or sum([matrix[i][col] for i in range(N)]) >= 1: return 0
    dx = [1,1,-1,-1]
    dy = [1,-1,1,-1]
    for i in range(4):
        for j in range(N):
            nx = row + (dx[i] * j) 
            ny = col + (dy[i] * j)
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1:
                    return 0
    return 1


def bt(row, matrix):
    global cnt
    if row == N:
        cnt += 1

    else:
        for i in range(N):
            if chk_line(row,i,matrix):
                matrix[row][i] = 1
                bt(row+1, matrix)
                matrix[row][i] = 0



N = int(input())
# N = 8
# print(N)

matrix = [[0] * N for _ in range(N)]


row = 0
cnt = 0
for i in range(N):
    matrix[row][i] = 1
    bt(row+1, matrix)
    matrix[row][i] = 0
print(cnt)



# 출처: https://rebas.kr/761 [PROJECT REBAS]
# n, ans = int(input()), 0
# a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

# def solve(i):
#     global ans
#     if i == n:
#         ans += 1
#         return
#     for j in range(n):
#         if not (a[j] or b[i+j] or c[i-j+n-1]):
#             a[j] = b[i+j] = c[i-j+n-1] = True
#             solve(i+1)
#             a[j] = b[i+j] = c[i-j+n-1] = False

# solve(0)
# print(ans)

