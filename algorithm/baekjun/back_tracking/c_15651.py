"""
백트래킹
N과 M 3
https://www.acmicpc.net/problem/15651
"""
def bt(N_list, cur, max_v, t_list):
    if cur == max_v:
        for i in t_list:
            print(i, end=' ')
        print()
    else:
        for i in range(len(N_list)):
            t_list.append(N_list[i])
            bt(N_list, cur + 1, max_v, t_list)
            t_list.pop(-1)

N, M = map(int, input().split())
# N, M = 4, 2
#print(N,M)

N_list = [i for i in range(1,N+1)]
#print(N_list)

cur = 0
t_list = []
bt(N_list, cur, M, t_list)