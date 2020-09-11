
def solution(a):
    if len(a) == 1:
        answer=1
    answer=2
    bool_T = [False] * len(a)
    L_start = a[0]
    for i in range(1,len(a)-1):
        if a[i] < L_start:
            L_start = a[i]
            answer+=1
            bool_T[i]=True

    R_start = a[-1]
    for i in range(len(a)-1,-1,-1):
        if a[i] < R_start:
            R_start = a[i]
            if bool_T[i]: continue
            answer+=1
            bool_T[i]=True

    return answer

# def dfs(a, cnt, save_val):
#     #print(a)
#     if len(a) == 1:
#         if a[0] not in save_val:
#             save_val.append(a[0])
#             print(save_val)
#     else:
#         for i in range(len(a)-1):
#             for j in range(2):
#                 if j != 0: # 0이 아니면 더작은 풍선 터트릴 수 있음
#                     if cnt == 0:
#                         continue
#                     if a[i] < a[i+1]:
#                         tmp_index = i   
#                     else:
#                         tmp_index = i+1
#                     tmp_val = a.pop(tmp_index)
#                     dfs(a, 0, save_val)
#                 elif j == 0: # 얘는 무조건 큰애들만 터뜨림
#                     if a[i] < a[i+1]:
#                         tmp_index = i+1
#                     else:
#                         tmp_index = i
#                     tmp_val = a.pop(tmp_index)
#                     dfs(a, cnt, save_val)
#                 a.insert(tmp_index,tmp_val)


# def solution(a):
#     save_val = list()

#     dfs(a, 1, save_val)
    
#     return len(save_val)


# a=[9,-1,-5]
# print(solution(a))

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))