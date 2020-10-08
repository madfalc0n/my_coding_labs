def solution(s):
    len_s = len(s)
    result = 0
    for i in range(len_s):
        tmp_cnt = 0
        for j in range(i+1,len_s):
            tmp_cnt = j - i
            if s[i] == s[j]:
                if tmp_cnt != 0:
                    tmp_cnt -= 1
            result += tmp_cnt
    
    return result

s = "baby"
print(solution(s))