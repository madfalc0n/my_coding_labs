#https://programmers.co.kr/learn/courses/30/lessons/42626
# 더맵게,,, 힙 문제

import heapq

def solution(scoville, K):
    heap = scoville
    if sum(heap) == 0:
        return -1
    len_s = len(scoville)
    cnt = 0
    while len_s != 1:
        f_min_list = heapq.heappop(heap)
        if f_min_list >= K:
            return cnt
        t_min_list = heapq.heappop(heap) * 2
        heapq.heappush(heap, f_min_list + t_min_list)
        len_s -= 1
        cnt += 1
    if heap[0] >= K:
        return cnt
    return -1

# test case
# scoville = [1, 2, 3, 9, 10, 12]
# scoville2 = [0, 0, 0, 0, 0, 0]
# scoville3 = [1,2,3] 
# k = 11
# print(solution(scoville, k))
# print(solution(scoville2, k))
# print(solution(scoville3, k))

# diff user
# import heapq as hq

# def solution(scoville, K):

#     hq.heapify(scoville)
#     answer = 0
#     while True:
#         first = hq.heappop(scoville)
#         if first >= K:
#             break
#         if len(scoville) == 0:
#             return -1
#         second = hq.heappop(scoville)
#         hq.heappush(scoville, first + second*2)
#         answer += 1  

#     return answer
