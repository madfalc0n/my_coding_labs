"""
평형저울
https://level.goorm.io/exam/43172/%ED%8F%89%ED%98%95-%EC%A0%80%EC%9A%B8/quiz/1
"""

def dfs(n, cost, cur_list, ori_list):
    global result
    if len(cur_list) == cost:
        print(cur_list, ori_list, sum(cur_list) + n, sum(ori_list))
        if sum(cur_list) + n == sum(ori_list):
            result = cur_list + [n] + [0] + ori_list
            print(result) 
    else:
        for i in range(len(ori_list)):
            tmp_val = ori_list.pop(i)
            dfs(n,cost, cur_list+[tmp_val], ori_list)
            ori_list.insert(i,tmp_val)


n = int(input())
c_list = [1,3,7,26,94,259]
result = []

for i in range(1,5):
    dfs(n,i,[], c_list)

print(result)

