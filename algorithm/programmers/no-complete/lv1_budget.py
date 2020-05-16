"""
예산문제
2018 여름/겨울 윈터 코딩
https://programmers.co.kr/learn/courses/30/lessons/12982
"""
from itertools import combinations,permutations

def dfs(d,length):
    
    visit = [d.pop(0)]



    return 0

def solution(d, budget):
    len_d = len(d)
    for i in range(len_d,0,-1):
        result = dfs(d,i)
        if result == 1:
            return i

        # tmp_list = list(combinations(d,i))
        # #print(tmp_list)
        # for tmp_list_d in tmp_list:
        #     if sum(tmp_list_d) <= budget:
        #         return i
    return 0

d = [1,3,2,5,4]	
budget = 9
print(solution(d,budget))