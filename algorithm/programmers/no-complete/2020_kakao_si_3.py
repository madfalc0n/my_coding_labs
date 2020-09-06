"""
4개의 보석을 모두 가지는 최소의 거리를 구하는 문제
https://programmers.co.kr/learn/courses/30/lessons/67258
"""


def solution(gems):
    uniq_gems = set(gems)
    len_uniq_list = len(uniq_gems)
    len_list = len(gems)
    if len_uniq_list == len_uniq_list:
        return [1,len_list]


    start = 0
    for i in range(len_list-len(uniq_gems)):

    print(gems)
    answer = []
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

print(set(gems))