"""
영어 끝말잊기
https://programmers.co.kr/learn/courses/30/lessons/12981
"""
def solution(n, words):
    number = 1
    people_cnt = 1
    proc_list = [words.pop(0)]
    while words:
        people_cnt += 1
        tmp_words = words.pop(0)
        if tmp_words in proc_list: # 똑같은 단어 말할 경우
            return [people_cnt,number]

        if proc_list[-1][-1] == tmp_words[0]: #일치할때
            proc_list.append(tmp_words)
        else: #끝나는 단어로 이어 말하지 않았을 경우
            return [people_cnt,number]
        
        if people_cnt == n:
            number += 1
            people_cnt = 0

    return [0,0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,words))