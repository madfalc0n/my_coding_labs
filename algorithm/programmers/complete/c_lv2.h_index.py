# H-index
#https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    if sum(citations) == 0:
        return 0
    h_index = 0
    i = 0
    while i <= len(citations):
        tmp_list = list(map(lambda x: x-i, citations))
        cnt = 0
        for val in tmp_list:
            if val >= 0:
                cnt += 1
        print(i,cnt, tmp_list)

        tmp_h_index = min(i, cnt)
        if h_index <= tmp_h_index:
            h_index = tmp_h_index
        i += 1

    return h_index


citations = [3, 0, 6, 1, 5]
print(solution(citations))
ci2 = [22, 42]
print(solution(ci2))


#다른 이들의 풀이
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0

#다른 이들의 풀이2
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer
