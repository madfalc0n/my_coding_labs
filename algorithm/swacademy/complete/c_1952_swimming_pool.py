"""
수영장
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE
22:08 시작
22:32 종료
"""
def check(start, total_val, pay):
    global price_list, use_list
    
    result_val = total_val
    next_point = start

    if pay == 0: # 1일
        tmp_val = use_list[start]
        result_val += (tmp_val * price_list[pay])
        next_point += 1
    elif pay == 1: #1달, 한달에 대한 이용료만 낸다, 다음으로 간다
        result_val += price_list[pay]
        next_point += 1
    
    elif pay == 2: #3달, 3달에 대한 이용료만 낸다, 3달뒤로 간다
        result_val += price_list[pay]
        next_point += 3 
    elif pay == 3: #1년, 1년은 전부 그냥 다 계산, 마지막으로 간다
        result_val += price_list[pay]
        next_point = 12

    return next_point, result_val


def dfs(start, total_val):
    global min_val
    
    if start >= len(use_list):
        min_val = min(min_val, total_val)

    else:
        for pay in range(4):
            cur, eval_val = check(start, total_val, pay)
            dfs(cur, eval_val)


tc = int(input())
for case in range(1, tc+1):
    #1일, 1달, 3달, 1년
    price_list = list(map(int,input().split()))
    use_list = list(map(int,input().split()))
    # print(price_list)
    # print(use_list)

    min_val = max(price_list) * sum(use_list)
    start = 0
    total_val = 0
    dfs(start, total_val)
    print(f"#{case} {min_val}")

