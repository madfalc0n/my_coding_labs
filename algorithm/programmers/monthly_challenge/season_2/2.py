def solution(s):
    answer = 0
    dict_list = {
        "[":"]",
        "{":"}",
        "(":")"
        }
    t_len = len(s)
    s = list(s)
    start = 0
    sw = 0
    while start < t_len:
        tmp_str = [s[0]]
        for i in range(len(s)-1):
            tmp_str.append(s[i+1])
            if len(tmp_str) > 1:
                # print(tmp_str, i)
                if dict_list.get(tmp_str[-2], 0) != 0:
                    if dict_list[tmp_str[-2]] == s[i+1]:
                        tmp_str.pop(-1)
                        tmp_str.pop(-1)


        if len(tmp_str) == 0:
            answer += 1

        tmp = s.pop(0)
        s.append(tmp)
        start += 1
        
    return answer

s= "}]()[{"
print(solution(s))