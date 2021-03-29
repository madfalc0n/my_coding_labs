"""
https://programmers.co.kr/learn/courses/30/lessons/12904?language=python3
"""



def solution(s):
    max_val = 0
    for i in range(1, len(s)-1):    
        print(i)
        if i // 2 == 0:
            f_list = s[:i]   
            b_list = s[i+1:]
        else:
            f_list = s[:i]   
            b_list = s[i+1:]

        print(f_list, b_list)
        f_list = f_list[::-1]
        tmp_len = min(len(b_list),len(f_list))
        tmp_val = 0
        for j in range(tmp_len):
            print(f_list[j], b_list[j])
            if f_list[j] == b_list[j]:
                tmp_val += 1
            else:
                break
        if tmp_val != 0:
            max_val = max(max_val , (tmp_val*2)+1)

    return max_val




st = 'aaaa'
# st = 'abcabbac'
print(solution(st))