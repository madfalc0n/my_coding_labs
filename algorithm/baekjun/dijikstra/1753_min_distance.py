"""
최단경로
https://www.acmicpc.net/problem/1753

"""

import heapq

def dij(start):
    d[start] = 0
    h_list = []
    heapq.heappush(h_list, [0, start])
    while h_list:
        cost, node = heapq.heappop(h_list)
        for cur_v, cur_w in m[node]:
            if d[cur_v] > cost + cur_w:
                d[cur_v] = cost + cur_w
                heapq.heappush(h_list, [d[cur_v], cur_v])

v, e = list(map(int, input().split(' ')))
start = int(input())
inf = 999999
d= [0] + ([inf] * v)

#memory out
# m = [[inf] * (v+1) for _ in range(v+1)]
# for i in range(e):
#     tu, tv, tw = list(map(int, input().split(" ")))
#     m[tu][tv] = tw

m = [[] for _ in range(1+v)]
for i in range(e):
    tu, tv, tw = list(map(int, input().split(" ")))
    m[tu].append([tv,tw])

dij(start)
for i in d[1:]:
    if i == inf:
        print('INF')
    else:
        print(i)