"""
백트래킹
N과 M 4
https://www.acmicpc.net/problem/15652
"""
def bt(N_list, cur, max_v, t_list):
    if len(t_list) == max_v:
        for i in t_list:
            print(i, end=' ')
        print()
    else:
        for i in range(cur, len(N_list)):
            t_list.append(N_list[i])
            bt(N_list, i, max_v, t_list)
            t_list.pop(-1)


N, M = map(int, input().split())
# N, M = 4, 2
#print(N,M)

N_list = [i for i in range(1,N+1)]
#print(N_list)

start = 0
t_list = []
bt(N_list, start, M, t_list)