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

def process_dfs(temp_list,v):
    pass

def process_bfs(temp_list,v):
    queue = []
    record = []
    queue.append(v)
    print(f"queue status : {queue}")
    while True:
        if len(queue) < 1:
            break
        proc_num = queue.pop(0)
        print(f"proc_num status : {proc_num}")
        print(f"queue status : {queue}")

        for i,data in enumerate(temp_list[proc_num-1]):
            if data == 1:
                if (i+1) not in queue:
                    queue.append(i+1)
                temp_list[proc_num-1][i] = 3
                temp_list[i][proc_num-1] = 3
            print(temp_list)
        print(f"end queue status : {queue}")
        record.append(proc_num)
    print(' '.join(record))
    #print(temp_list)





node, line, v = map(int, input().split(' '))
print(node, line, v)
temp_list = []
for i in range(node):
    temp = [0 for j in range(node)]
    temp_list.append(temp)
print(temp_list)

for i in range(line):
    node1, node2 = map(int, input().split(' '))
    temp_list[node1-1][node2-1] = 1
    temp_list[node2-1][node1-1] = 1
print(temp_list)

process_dfs(temp_list,v)
process_bfs(temp_list,v)

