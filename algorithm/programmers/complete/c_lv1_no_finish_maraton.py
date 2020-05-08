"""
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576
"""

#다른사람 풀이
import collections


def solution(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]



# #내풀이
# def solution(participant, completion):
#     participant_set = {}
#     for people in participant:
#         participant_set[people] = participant_set.get(people,0) + 1
    
#     for complete in completion:
#         participant_set[complete] -= 1
    
#     result = [people for people in participant_set.keys() if participant_set[people] != 0  ]

#     return result.pop(0)

participant = ['mislav', 'stanko', 'mislav', 'ana'] 
completion = ['stanko', 'ana', 'mislav']
print(solution(participant,completion))