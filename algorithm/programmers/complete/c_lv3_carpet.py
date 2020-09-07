"""
카펫
https://programmers.co.kr/learn/courses/30/lessons/42842
"""

def solution(brown, yellow):
    p_list = [(i,yellow//i) for i in range(1, yellow+1) if yellow % i == 0]


    print(p_list)

    for i in p_list:
        if 2 * (i[0] + i[1] + 2) == brown:
            return [max(i)+2,min(i)+2]
    

brown = 24
yellow = 24

print(solution(brown,yellow))