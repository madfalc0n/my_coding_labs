"""
벽은 처음 길이의 각 행,열 길이만큼 곱해짐
[[1,1,2,1],[2,1,2,2],[2,2,2,3],[1,2,1,3],[2,2,1,2]]
맵짜고 + bfs
"""
def bfs(n_maze, visit):
    return 1

def solution(rows, columns, maze, r1, c1, r2, c2):
    n_maze = maze.copy()
    for row in range(rows, rows*rows , rows):
        for m in maze:
            n_maze.append([m[0]+row, m[1], m[2]+row, m[3]])
    for col in range(columns, columns*columns , columns):
        for m in maze:
            n_maze.append([m[0], m[1]+col, m[2], m[3]+col])
    for i in n_maze:
        print(i)
    
    visit = []
    result = bfs(n_maze,visit)
    
    return result


rows = 2
columns = 3 
maze  = [[1,1,2,1],[2,1,2,2],[2,2,2,3],[1,2,1,3],[2,2,1,2]]
r1,c1,r2,c2 = 3,1,1,9
print(solution(rows, columns, maze, r1, c1, r2, c2))

rows = 3
columns = 3 
maze  = [[1,1,1,2],[1,2,2,2],[1,3,2,3],[2,2,2,3],[2,1,2,2],[2,1,3,1],[2,2,3,2],[3,2,3,3]]
r1,c1,r2,c2 = 9,1,1,9
print(solution(rows, columns, maze, r1, c1, r2, c2))