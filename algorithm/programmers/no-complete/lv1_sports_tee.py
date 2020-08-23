"""
체육복
https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
"""

def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in lost:
        if len(reserve) == 0:
            return answer
        
        tmp_v = i
        if tmp_v in reserve:
            reserve.pop(reserve.index(tmp_v))
            continue

        elif tmp_v-1 in reserve and tmp_v-1 > 0:
            answer += 1
            reserve.pop(reserve.index(tmp_v+1))
            continue
            
        elif tmp_v+1 in reserve:
            answer += 1
            reserve.pop(reserve.index(tmp_v+1))
            continue
            
    return answer
