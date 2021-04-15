def bfs(start,computers):
    visit = [start]
    queue = [start]
    while queue:
        val = queue.pop(0)
        for com in range(1, len(computers[val])):
            if com != val:
                if com not in visit and computers[val][com] == 1:
                    queue.append(com)
                    visit.append(com)
    return set(visit)

def solution(n, computers):
    answer = 0
    computers = [0] + computers
    for i in range(1,len(computers)):
        computers[i] = [0] + computers[i]
    # print(computers)    
    start = 1
    cur = 1
    all_list = set(list(range(1,n+1)))
    visit = set()
    while len(all_list) > 1:
        visit = bfs(start,computers)
        all_list = all_list - visit
        start = list(all_list)[0]
        cur += 1
        
    return cur

n =3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))