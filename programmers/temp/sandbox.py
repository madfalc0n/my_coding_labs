# #5번 돌 건너기
# def solution(stones, k):
#     answer = 0
#     return answer













#4번 호텔 방 배정문제(효율성)
def sol2(diff_len, list_set_room_number):
    print("함수 2 전환")
    print(diff_len, list_set_room_number)
    i = 0
    temp_list = []
    while i < len(list_set_room_number):
        if i == 0:
            temp_list.append(list_set_room_number[i] - 1)
        else: # 0보다 클 경우
            temp_list.append(list_set_room_number[i] - list_set_room_number[i-1] - 1)
        if sum(temp_list) >= diff_len: # 조기 종료
            break
        i+= 1

    if sum(temp_list) < diff_len:
        print("합이 모자라서 채움")
        temp_list.append(diff_len -  sum(temp_list))
    print(list_set_room_number)
    print(temp_list)
    print("함수2 전환완료")
    return temp_list

def sol3(temp_list, list_set_room_number):
    temp_num_list = []
    for i,num in enumerate(temp_list):
        if i == 0 and num != 0:
            print(list_set_room_number[i],num)
            for n in range(1, list_set_room_number[i] ):
                temp_num_list.append(n)

        if i != 0 and num != 0:
            print(list_set_room_number[i-1],num)
            for n in range(list_set_room_number[i-1]+1, list_set_room_number[i-1]+num+1 ):
                temp_num_list.append(n)
            #temp_num_list += [ num2 for num2 in range(list_set_room_number[i-1]+1, list_set_room_number[i-1]+num+1) ]
    print("temp_num_list: ", temp_num_list)
    return temp_num_list


def solution(k, room_number):
    set_room_number = set(room_number)
    if len(room_number) == len(set_room_number): # 중복이 없을 경우
        return room_number

    result = []

    diff_len = (len(room_number) - len(set_room_number))
    list_set_room_number = list(set_room_number)

    temp_list = sol2(diff_len, list_set_room_number)
    temp_num_list = sol3(temp_list, list_set_room_number)
    

    for i in room_number:
        if i in result:
            result.append(temp_num_list.pop(0))
        else:
            result.append(i)

    return result


k = 10
room_number = [4,4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,]

print(solution(k,room_number))

# """
# 1. 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.

# 2. 고객은 투숙하기 원하는 방 번호를 제출합니다.

# 3. 고객이 원하는 방이 비어 있다면 즉시 배정합니다.

# 4. 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.
# """









# #2번 집합문제
# def preprocessing(s): #문자열 전처리를 통해 배열로 저장하기위한 함수
#     conv_s = []
#     s = s[1:-2]
#     s = s.replace('{','')
#     s = s.split('},')
#     for i in s:
#         temp = i.split(',')
#         str2num = set([ int(num) for num in temp ])
#         conv_s.append(str2num)
#     return conv_s

# def solution(s):
#     result = []
#     s = preprocessing(s)
#     print(f"전처리된 s 값: {s}")

#     num_cnt_list = [ len(num) for num in s ]
#     print(num_cnt_list)

#     len_string = len(s)
#     cnt = 1
#     temp = []
#     for i in range(1,len_string+1):
#         num_cnt_list.index(i) #집합 위치 작은순으로 찾음
#         temp.append(s[num_cnt_list.index(i)]) #임시 리스트에 저장
#         if i != 1:
#             temp_diff_v = s[num_cnt_list.index(i)] - s[num_cnt_list.index(i-1)]
#             print(temp_diff_v)
#             result.append(list(temp_diff_v)[0])
#         else:
#             result.append(list(s[num_cnt_list.index(cnt)])[0])
#     return result

# s = "{{2},{2,1,3},{2,1},{2,1,3,4}}"
# print(solution(s))





# #1번 인형뽑기 문제
# def solution(board, moves):
#     same_cnt = 0
#     stack = []
#     for i in moves:
#         move_num = i-1
#         for j in board:
#             if j[move_num] != 0: #인형뽑고 stack에 저장
#                 temp = j[move_num]
#                 #print(f"{i}번에서 뽑아올려 스택에 {j[move_num]}을 저장")
#                 j[move_num] = 0
#                 #stack에 저장되어있는 마지막 값 비교
#                 if len(stack) !=0 and stack[-1] == temp:
#                     same_cnt += 1
#                     #print("같은거 뽑음")
#                     stack.pop()
#                 else:
#                     stack.append(temp)
#                 break
#     return same_cnt*2


# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
# moves = [1,5,3,5,1,2,1,4]
# print(solution(board,moves))

