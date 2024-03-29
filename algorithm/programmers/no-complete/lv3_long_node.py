"""
https://programmers.co.kr/learn/courses/30/lessons/49189
가장 먼 노드를 찾기
1.dfs를 통해 최대 거리를 구한다.
2.1번과 연결되어 있지 않는 애들을 구한다.
"""

def pr(list):
    for i in list:
        print(i)

def bfs(matrix, v_matrix, cnt_matrix ,start, cnt):
    v_matrix[start] = 1
    cnt_matrix[start] = cnt
    queue = [start]
    while queue:
        cnt += 1
        cur = queue.pop(0)
        for i in range(2,len(matrix[cur])):
            if v_matrix[i]:
                cnt_matrix[i] = min(cnt, cnt_matrix[i])
                continue
            if matrix[cur][i] == 1 and v_matrix[i] == 0:
                v_matrix[i] = 1
                cnt_matrix[i] = cnt
                queue.append(i)
                continue


def solution(n, edge):
    matrix = [[0] * (n+1) for _ in range(n+1)]
    v_matrix = [0] * (n+1)
    cnt_matrix = [0] * (n+1)

    for i in edge:
        matrix[i[0]][i[1]] = 1 
        matrix[i[1]][i[0]] = 1 
    pr(matrix)
    start = 1
    v_matrix[start] = 1
    cnt_matrix[start] = 1
    cnt = 1
    for i in range(1, len(matrix[start])):
        if matrix[start][i] == 1:
            bfs(matrix, v_matrix, cnt_matrix ,i, cnt+1)

    print(v_matrix)
    print(cnt_matrix)

    return cnt_matrix.count(max(cnt_matrix))

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# n = 5
# vertex = [[1, 2], [1, 3], [1, 4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]	
print(solution(n,vertex))


# def bfs(matrix,visit_matrix,start):
#     cnt = 1
#     visit_matrix[start] = cnt    
#     visit = [start]
#     queue = [start]
#     while queue:
#         point = queue.pop(0)
#         for i in range(1,len(matrix)):
#             if matrix[point][i] == 1 and i not in visit: #간선으로 연결되어 있고 방문한적이 없다?
#                 visit_matrix[i] = visit_matrix[point] + 1
#                 visit.append(i)
#                 queue.append(i)
#     #print(f"visit : {visit}")
#     #print(f"visit_matrix : {visit_matrix}")
#     max_val = max(visit_matrix)
#     return visit_matrix.count(max_val)




# def print_list(list):
#     for i in list:
#         print(i)

# def solution(n, edge):
#     matrix = [[0] * (n+1) for _ in range(n+1)] #빈 매트릭스 생성
#     visit_matrix = [0 * (n+1) for _ in range(n+1)]
#     for vertex in edge: #간선 표시
#         matrix[vertex[0]][vertex[1]] = 1
#         matrix[vertex[1]][vertex[0]] = 1
#     #print_list(matrix)

#     long_node = []
#     for i in range(2,n+1):
#         if matrix[i][1] == 0 : #1과 떨어져있을 경우
#             long_node.append(i)
#     print(long_node)

#     start = 1
#     result = bfs(matrix,visit_matrix,start)
#     return result


# n = 6
# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	
# print(solution(n,vertex))