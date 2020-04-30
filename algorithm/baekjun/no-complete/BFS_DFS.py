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

def dfs(matrix,start):#스택이용
    print(f"{start}",end=' ')
    visit[start] = 1
    for find_node in range(1,len(matrix[start])):
        #print(f"start : {start} find_node : {find_node} visit : {visit}")
        if matrix[start][find_node] and visit[find_node] == 0: #매트릭스에서 간선으로 연결되어있고 방문한적이없는경우 탐색
            dfs(matrix,find_node)

def bfs(matrix,start):
    visit = []
    queue = [start]
    while queue:
        #print(f"queue : {queue}")
        #print(f"visit : {visit}")
        node = queue.pop(0)
        if node not in visit: #노드가 방문한적이 없다면?
            visit.append(node)
            queue += [i for i in range(1,len(matrix[node])) if matrix[node][i] == 1 and i not in queue and i not in visit]
        #print(f"{node}", end=' ')
    visit = list(map(str,visit))
    print(' '.join(visit))


node, line, start = map(int,input().split(' '))
print(node,line,start)
visit = [0] * (node+1)

matrix = [[0]*(node+1) for i in range(node+1)] #0번쨰는 사용하지 않는다.

for i in range(line):
    node = list(map(int,input().split(' ')))
    matrix[node[0]][node[1]] = 1
    matrix[node[1]][node[0]] = 1
# for i in matrix:
#     print(i)

#print(visit) #0번째는 사용하지 않는다
#print(matrix,start)
dfs(matrix,start)
print()
#print(matrix,start)
bfs(matrix,start)