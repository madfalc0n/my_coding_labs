import heapq

def solution(a, edges):
    if sum(a) != 0 :
        return -1

    if a.count(0) == len(a):
        return 0

    answer = -2
    num = len(a)
    matrix = [[] for _ in range(num)]
    dict_list = {}
    
    for edge in edges:
        s,e = edge
        dict_list[s] = dict_list.get(s,0) + 1
        dict_list[e] = dict_list.get(e,0) + 1
        matrix[s].append(e)
        matrix[e].append(s)
    
    print(matrix)
    print(dict_list)
    tmp_dict_list = sorted(dict_list.items(), key= lambda x: x[1])
    print(tmp_dict_list)
    queue = []
    queue_list = [False] * num
    for dl in tmp_dict_list:
        if dl[1] != 1:
            break
        else:
            queue.append(dl)
    visit = [False] * num
    cnt = 0
    while queue:
        node,_ = queue.pop(0)
        visit[node] = True
        queue_list[node] = True
        if a[node] == 0:
            continue
        else:
            for end in matrix[node]:
                if visit[end] == False and queue_list[end] == False:
                        a[end] += a[node]
                        cnt += abs(a[node])
                        a[node] = 0
                        queue.append([end,_])     
                                   
                    
    if sum(a) != 0:
        return -1
    return cnt

a = [-5,0,2,1,2]
e = [[0,1],[3,4],[2,3],[0,3]]
# a = [0,1,0]
# e = [[0,1],[1,2]]

print(solution(a,e))