"""
테트로미노
https://www.acmicpc.net/problem/14500
구현문제
16:43 시작
17:29 종료
참고 https://jeongchul.tistory.com/670
"""
def pr(list):
    for i in list:
        print(i)

tetromino = [
    [(0,0),(0,1),(1,0),(1,1)], # ㅁ
    [(0,0),(0,1),(0,2),(0,3)], # ㅡ
    [(0,0),(1,0),(2,0),(3,0)], 
    [(0,0),(0,1),(0,2),(1,0)], # ㄱ
    [(0,2),(1,0),(1,1),(1,2)], 
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,2)],
    [(0,0),(1,0),(2,0),(2,1)],
    [(0,1),(1,1),(2,0),(2,1)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(0,1),(0,2),(1,1)], #ㅗ 
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(1,1),(2,0)],
    [(0,1),(1,0),(1,1),(2,1)],
    [(0,1),(1,0),(1,1),(2,0)], #ㄹ
    [(0,0),(1,0),(1,1),(2,1)],
    [(1,0),(1,1),(0,1),(0,2)],
    [(0,0),(0,1),(1,1),(1,2)],
]
# print(len(tetromino))
N, M = list(map(int,input().split()))
matrix = [ list(map(int,input().split())) for _ in range(N)]
# pr(matrix)
result = 0
for i in range(N):
    for j in range(M):
        for t_list in tetromino:
            cnt = 0
            tmp_result = 0
            for point in range(4):
                tmp_x = i + t_list[point][0]
                tmp_y = j + t_list[point][1]
                if tmp_x in range(N) and tmp_y in range(M):
                    cnt += 1
                    tmp_result += matrix[tmp_x][tmp_y]
                else:
                    break
            result = max(result, tmp_result)
print(result)