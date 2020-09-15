"""
백트래킹
N과 M 2
https://www.acmicpc.net/problem/15650
"""

def check_dup(t_list, s_list):
    for i in s_list:
        if len(set(t_list) - set(i)) == 0: #비교 결과 같지않을 경우, 0이 아니면 서로 다른것으로 간주
            return 1
    return 0

def bt(N_list, cur, max_v, t_list, s_list):
    if cur == max_v:
        cpy_t_list = t_list.copy()
        if check_dup(cpy_t_list, s_list): # 중복 있으면 건너뜀
            pass
        else:
            s_list.append(cpy_t_list)
    else:
        for i in range(len(N_list)):
            if N_list[i] in t_list:
                continue
            t_list.append(N_list[i])
            bt(N_list, cur + 1, max_v, t_list, s_list)
            t_list.pop(-1)


N, M = map(int, input().split())
# N, M = 4, 2
#print(N,M)

N_list = [i for i in range(1,N+1)]
#print(N_list)

cur = 0
t_list = []
s_list = []
bt(N_list, cur, M, t_list, s_list)
#print(s_list)
for i in s_list:
    for j in i:
        print(j,end=' ')
    print()