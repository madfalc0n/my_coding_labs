"""
퇴사
https://www.acmicpc.net/problem/14501
DP, 브루트포스
"""

# 다른사람이 dp로 푼거
# N = int(input())
# table = list(list(map(int, input().split())) for _ in range(N))
# dp = [0] * N

# for i in range(N):
#     if i + table[i][0] <= N:
#         dp[i] = table[i][1]
#         for j in range(i):
#             if j + table[j][0] <= i:
#                 dp[i] = max(dp[i], dp[j] + table[i][1])

# print(max(dp))



def dfs(start, cost, pre):
    global N
    global result
    global talk_list

    if start == N: # N == 8 일때
        result = max(cost,result) 
    elif start > N: # start 8보다 클때, 상담이 안되므로 이전꺼 뺌
        tmp_cost = cost - talk_list[pre][1]
        result = max(tmp_cost,result)
    else:
        for cur in range(start,N):
            day = talk_list[cur][0] + cur
            cost_2 = talk_list[cur][1] + cost
            dfs(day, cost_2, cur)
            
N = int(input())
talk_list = [[0,0]]
for i in range(N):
    talk_list.append(list(map(int, input().split())))

# N = 8
N += 1
talk_list.append([0,0])

result = 0

for i in range(1,N):
    day = talk_list[i][0] + i
    cost = talk_list[i][1]
    if day <= N:
        dfs(day, cost, i)
print(result)