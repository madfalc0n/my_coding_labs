
# set으로 푸니까 기록 겁나 빠름 굿 
# 에라토스체네스의 체
import math

def solution(n): # 100일떄
    cal_len = math.ceil(math.sqrt(n))
    print(cal_len)
    print(math.ceil(math.sqrt(cal_len)))
    r_list = set(range(2,n+1))
    i = 2

    while True:
        if i not in r_list: # 있으면 진행 없으면 한번더 +1
            print(f"{i}는 이미 삭제되고 없음")
            i +=1
            continue
        cal_set = set([  j for j in range(2*i,n+1, i) ])
        r_list.difference_update(cal_set)
        i += 1
        print(r_list)
        if i >= cal_len:
            break

    #print(r_list)
    return len(r_list)

n = 100

print(solution(n))


# # 에라토스체네스의 체
# import math

# def solution(n): # 100일떄
#     cal_len = math.ceil(math.sqrt(n))
#     print(cal_len)
#     print(math.ceil(math.sqrt(cal_len)))
#     r_list = []
#     first_c = 2
#     for i in range(2,n+1): # 소수를 검사하는 전체 반복
#         cnt = 0
#         for j in range(2, cal_len+1): #소수인지 아닌지
#             if j > math.sqrt(i)  and i //j == 1: # 소수인경우
#                 print(i, j )
#                 break
#             if i%j == 0: #소수가 아닌경우
#                 cnt += 1
#                 break
#         if cnt == 0: # 소수 인 애를 뽑는다.
#             r_list.append(i)

#     print(r_list)
#     return len(r_list)






# n = 100

# print(solution(n))