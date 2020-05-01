"""
백준 1260번
BFS ....
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
첫째 줄에 정점(노드)의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
"""

def dfs(matrix,start): #재귀 이용
    print(f"{start}",end=' ')
    visit[start] = 1
    for find_node in range(1,len(matrix[start])):
        #print(f"start : {start} find_node : {find_node} visit : {visit}")
        if matrix[start][find_node] and visit[find_node] == 0: #매트릭스에서 간선으로 연결되어있고 방문한적이없는경우 탐색
            dfs(matrix,find_node)


def bfs(matrix,start):
    #print(f"{start}",end=' ')
    #print(node)
    visit = [start]
    queue = [start]
    while queue:
        start = queue.pop(0)
        for i in range(1,len(matrix)):
            if matrix[start][i] == 1 and i not in visit: #선으로 연결되어있고 방문한 적이 없는놈인 경우
                visit.append(i)
                queue.append(i)
    visit = list(map(str,visit))
    print(' '.join(visit))



node, line, start = map(int,input().split(' '))
#print(node,line,start)
visit = [0] * (node+1)

matrix = [[0]*(node+1) for i in range(node+1)] #0번쨰는 사용하지 않는다.

for i in range(line):
    node_l = list(map(int,input().split(' ')))
    matrix[node_l[0]][node_l[1]] = 1
    matrix[node_l[1]][node_l[0]] = 1
# for i in matrix:
#     print(i)

#print(visit) #0번째는 사용하지 않는다
#print(matrix,start)
dfs(matrix,start)
print()
#print(matrix,start)
bfs(matrix,start)