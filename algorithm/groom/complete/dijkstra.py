"""
다익스트라 알고리즘
https://level.goorm.io/exam/43211/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-dijkstra-s-algorithm/quiz/1

input :
3 4
1 2 5
1 3 4
2 3 2
2 3 1
1

output :
1: 0
2: 5
3: 4

"""

import heapq


def dij(start):
    h_list = [[0,start]]
    d[start] = 0
    while h_list:
        cost,node = heapq.heappop(h_list)
        for cur_node, cur_cost in m[node]:
            tmp_cost = cur_cost + cost
            if d[cur_node] > tmp_cost:
                d[cur_node] = tmp_cost
                heapq.heappush(h_list, [ tmp_cost, cur_node])

inf = 999999999
n, e = list(map(int, input().split(' ')))
m = [[] for _ in range(n+1)]
d = [inf] * (n+1)
for i in range(e):
    sn, tn, c = list(map(int,input().split(' ')))
    m[sn].append([tn,c])
    m[tn].append([sn,c])

start = int(input())
dij(start)
for i in range(1,n+1):
    print(f"{i}: {d[i]}")

