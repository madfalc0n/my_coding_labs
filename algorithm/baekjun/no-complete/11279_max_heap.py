#https://www.acmicpc.net/problem/11279
# 배열에 자연수 x 넣는다.
# 0입력 시 가장 큰값을 출력하고 그 값을 배열에서 제거한다.

n_input = int(input())
arr_list = [0]
max_val = 0

while (n_input):
    tmp_input = int(input())
    tmp_len = len(arr_list)
    if tmp_input == 0: # 입력값 0일때 제일 큰거 삭제
        if tmp_len == 1: print("0")
        else: print(arr_list.pop(1))
    else: #입력값 자연수 일때 저장
        if tmp_input >= max_val:
            max_val = tmp_input
            arr_list.insert(0, tmp_input)
        else:
            tmp_cnt = 0 
            i = 0
            while (i < tmp_len):
                if tmp_input > arr_list[i]:
                    arr_list.insert(i, tmp_input)
                    tmp_cnt = 1
                    break
                i += 1
            if tmp_cnt == 0: arr_list.insert(i, tmp_input)
            
    n_input -= 1