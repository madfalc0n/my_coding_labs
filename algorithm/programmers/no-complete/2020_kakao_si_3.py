"""
4개의 보석을 모두 가지는 최소의 거리를 구하는 문제

"""
import collections
# def solution(participant, completion):
#     print(collections.Counter(participant))
#     print(collections.Counter(completion))
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

def solution(gems):
    dict_list = collections.Counter(gems)
    print(dict_list)
    answer = []
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))