"""
숫자 만들기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeRZV6kBUDFAVH&categoryId=AWIeRZV6kBUDFAVH&categoryType=CODE
21:29 시작
22:07 종료
"""
def check(cur, key, eval_val):
    global number_list

    result_val = eval_val
    
    if key == 0 :# +
        result_val += number_list[cur]
    elif key == 1:#-
        result_val -= number_list[cur]
    elif key == 2:# *
        result_val *= number_list[cur]
    elif key == 3:# /
        # result_val = int(result_val)
        result_val /= number_list[cur]
        result_val = int(result_val)

    return result_val

def dfs(eval_dict, cur, eval_val):
    global n, max_val, min_val
    
    if cur == n: #모든 수를 더했을 경우
        # print(eval_val)
        if eval_val > 0:
            if eval_val > int(eval_val):
                eval_val += 1
        elif eval_val < 0:
            if eval_val < int(eval_val):
                eval_val -= 1
        eval_val = int(eval_val)

        max_val = max(max_val, eval_val)
        min_val = min(min_val, eval_val)
    else:
        for key in eval_dict.keys():
            if eval_dict[key] != 0: #0이 아닐 때 사용
                eval_dict[key] -= 1
                result_val = check(cur, key, eval_val)
                dfs(eval_dict , cur+1, result_val)
                eval_dict[key] += 1
            

tc = int(input())
for case in range(1,tc+1):
    n = int(input())
    max_val = -100000000
    min_val = 100000000
    # 0 + ,1 - ,2 * ,3 / 순으로 
    eval_list = list(map(int,input().split()))
    number_list = list(map(int,input().split()))
    
    eval_dict = dict()
    for i in range(4):
        eval_dict[i] = eval_list[i]
    # print(eval_dict)
    
    start = 1
    eval_val = number_list[0]
    dfs(eval_dict, start, eval_val)
    # print(max_val)
    # print(min_val)
    print(f"#{case} {max_val - min_val}")