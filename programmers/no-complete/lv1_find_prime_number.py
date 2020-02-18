# 에라토스체네스의 체
import math

def solution(n): # 100일떄
    cal_len = math.ceil(math.sqrt(n))
    print(cal_len)
    print(math.ceil(math.sqrt(cal_len)))
    r_list = []
    for i in range(2,n+1): # 소수를 검사하는 전체 반복
        cnt = 0
        for j in range(2, cal_len+1): #소수인지 아닌지
            if j > math.sqrt(i)  and i //j == 1:
                break
            if i%j == 0:
                cnt += 1
        if cnt == 0:
            r_list.append(i)

    print(r_list)
    return len(r_list)

n = 5

print(solution(n))