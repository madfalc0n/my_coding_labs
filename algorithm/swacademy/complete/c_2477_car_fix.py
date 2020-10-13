"""
차량정비소
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV6c6bgaIuoDFAXy&categoryId=AV6c6bgaIuoDFAXy&categoryType=CODE

참고: https://hongsj36.github.io/2020/02/27/SWEA_2477/
"""

tc = int(input())
for case in range(1,tc+1):
    # 접수 창구 갯수, 정비 창구 갯수, 정비소방문고객수, 지갑두고간고객이용접수 창구, 지갑두고간고객이용정비 창구
    N,M,K,A,B = list(map(int,input().split()))
    
    # a 창구 
    a_list = list(map(int,input().split()))
    
    # b 창구 
    b_list = list(map(int,input().split()))
    
    #정비소 방문 고객
    v_list = list(map(int,input().split()))
    
    # a,b를 각각 -1, 인덱스는 0부터 시작하므로
    A, B =  A-1, B-1
    a_wait_list = [] # a 대기열
    a_state = [None] * N # a 창구들 상태
    a_num = 0 # a 창구 인원
    
    b_wait_list = [] # b 대기열
    b_state = [None] * M # b 창구들 상태
    b_num = 0 # b 창구 인원

    result_list = [False] * K
    result = 0

    time = 0
    index = 0 # 방문고객 번호
    while v_list or a_num or b_wait_list:

        # 대기손님 a 대기열로
        while v_list and v_list[0] == time:
            v_list.pop(0)
            a_wait_list.append(index)
            index += 1

        # a 대기열 -> a 창구 -> b 대기열
        for i in range(N):
            # a 창구 i번에 있을 경우
            if a_state[i]:
                a_state[i][1] -= 1 # 시간 감소
                if a_state[i][1] == 0: #시간 감소 후 0초 되면 업무완료
                    b_wait_list.append(a_state[i][0])
                    a_state[i] = None
                    a_num -= 1

            if a_state[i] is None:
                if a_wait_list:
                    tmp_user_num = a_wait_list.pop(0)
                    a_state[i] = [tmp_user_num, a_list[i]]
                    a_num += 1
                    if i == A: #지갑 떨어뜨린 창구이면
                        result_list[tmp_user_num] = True

    
        for i in range(M):
            # a 창구 i번에 있을 경우
            if b_state[i]:
                b_state[i][1] -= 1 # 시간 감소
                if b_state[i][1] == 0: #시간 감소 후 0초 되면 업무완료
                    b_state[i] = None

            if b_state[i] is None:
                if b_wait_list:
                    tmp_user_num = b_wait_list.pop(0)
                    b_state[i] = [tmp_user_num, b_list[i]]
                    if i == B and result_list[tmp_user_num]: #지갑 떨어뜨린 창구이면
                        result += (tmp_user_num+1)
        time += 1
    if not result:
        result = -1
    
    print(f"#{case} {result}")