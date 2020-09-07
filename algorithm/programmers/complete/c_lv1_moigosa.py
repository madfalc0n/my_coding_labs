"""
https://programmers.co.kr/learn/courses/30/lessons/42840
모의고사
"""
def solution(answers):
    user_1 = [1, 2, 3, 4, 5] # 5
    user_1_len = len(user_1)
    user_2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    user_2_len = len(user_2)
    user_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    user_3_len = len(user_3)
    score = [0,0,0]
    for i,d in enumerate(answers):
        u_1_val = i % user_1_len 
        u_2_val = i % user_2_len
        u_3_val = i % user_3_len
        if user_1[u_1_val] == d:
            score[0] += 1
        if user_2[u_2_val] == d:
            score[1] += 1
        if user_3[u_3_val] == d:
            score[2] += 1
    max_val = max(score)
    result = [ i+1 for i in range(3) if score[i] == max_val]
    return result

answers = [1,3,2,4,2]
print(solution(answers))