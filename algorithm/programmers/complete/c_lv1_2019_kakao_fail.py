"""
https://programmers.co.kr/learn/courses/30/lessons/42889
실패율
"""

def solution(N, stages):
    stage_dict = dict()

    for i in range(1,N+1):
        com_s = 0
        cur_s = 0
        for j in stages:
            if i == j:
                cur_s += 1
                com_s += 1
            elif i < j:
                com_s += 1
        if com_s == 0:
            stage_dict[i] = 0
        else:
            stage_dict[i] = cur_s / com_s
    result = list(sorted(stage_dict.items(), key= lambda x: x[1], reverse=True))

    return list(map(lambda x: x[0], result))

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4,4,4,4,4]
N=8
stages=[1,2,3,4,5,6,7]
print(solution(N, stages))
