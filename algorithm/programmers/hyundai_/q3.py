def solution(s):
    save_s = s
    max_a = 'a'
    max_i = 2000000
    for i in range(len(s)):
        if max_a <= s[i]:
            max_a = s[i]
            max_i = i
    
    # print(f"max_a : {max_a}, max_i : {max_i}")
    for i in range(max_i+1):
        for j in range(i+1):
            tmp_s_1 = s[j:i+1]
            tmp_s_1 = tmp_s_1[::-1]
            tmp_s_2 = s[i+1:]
            # print(f"i : {i}, j : {j}")
            # print(f"tmp_s_1 : {tmp_s_1}")
            # print(f"tmp_s_2 : {tmp_s_2}")
            if j != 0:
                tmp_s_1 = s[:j] + tmp_s_1
            tmp_s = tmp_s_1 + tmp_s_2
            # print(f"tmp_s_1 + tmp_s_2 : {tmp_s}")
            if tmp_s > save_s:
                save_s = tmp_s
            
    return save_s