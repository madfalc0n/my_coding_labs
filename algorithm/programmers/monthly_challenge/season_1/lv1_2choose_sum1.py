"""
2개 뽑아서 더하기
https://programmers.co.kr/learn/courses/30/lessons/68644
"""

def solution(n):
    if n < 3:
        return n
    answer = 0
    tmp_list = []
    while 1:
        a = n // 3
        b = n % 3
        n = a
        tmp_list.append(b)
        if n < 3:
            tmp_list.append(a)
            break
    # print(tmp_list)
    cnt =0
    for i in range(len(tmp_list)-1,-1,-1):
        answer += tmp_list[i] * (3**cnt)
        cnt += 1
    return answer

print(solution(1))