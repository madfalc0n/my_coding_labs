"""
4개의 보석을 모두 가지는 최소의 거리를 구하는 문제
https://programmers.co.kr/learn/courses/30/lessons/67258
"""


def solution(gems):
    start, end = 0, 0
    uniq_gem = len(set(gems))
    len_gem = len(gems)
    gem_dict = dict()
    candidate = list()
    #print(uniq_gem)
    
    while True:
        if end >= len_gem and len(gem_dict) != uniq_gem: #보석 길이보다 넘을 경우
            break
        if len(gem_dict) != uniq_gem and end < len_gem: #모든 보석 종류 등록할 때 까지 end 증가
            gem_dict[gems[end]] = gem_dict.get(gems[end],0) + 1
            end += 1
        
        if len(gem_dict) == uniq_gem : #모든 보석종류 넣을 경우 start 증가
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0: # -1 햇는데 0이 될 경우 모든 보석 종류 중 하나를 삭제, 즉 현재 포인트 저장
                del gem_dict[gems[start]]
                candidate.append([start+1,end])
            start += 1
        
    #print(candidate)
    result_list = []
    for i in candidate:
        tmp_cost = i[1] - i[0] + 1
        result_list.append(tmp_cost)

    #print(result_list)
    min_index = result_list.index(min(result_list))

    return candidate[min_index]


gems = ["DIA", "EM", "EM", "RUB", "DIA"]
print(solution(gems))
gems = ["DIA", "DIA", "DIA", "DIA", "EMERALD", "SAPPHIRE", "RUBY", "RUBY"]
print(solution(gems))
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
