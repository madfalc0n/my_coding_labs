def chk(val):
    if val == 6:
        return 1
    elif val == 5:
        return 2
    elif val == 4:
        return 3
    elif val == 3:
        return 4
    elif val == 2:
        return 5
    else:
        return 6
    

def solution(lottos, win_nums):
    lottos = sorted(lottos)
    win_nums = sorted(win_nums)

    if lottos.count(0) == 6:
        return [1,6]
    if lottos == win_nums:
        return [1,1]
    
    l_set = set(lottos)
    zero_cnt = lottos.count(0) # 0의 개수 = 확률 업
    w_set = set(win_nums)
    correct_cnt = len(l_set & w_set) # 교집합의 개수 = 당첨 수  
    
    max_p = chk(zero_cnt + correct_cnt)
    min_p = chk(correct_cnt)
        
    answer = [max_p,min_p]
    
    return answer