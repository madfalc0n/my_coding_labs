# #5번 태그 일치하는 문서 찾기
# def solution(dataSource, tags):
#     answer = []
#     temp_dict = {}
#     for tag in tags:
#         for data in dataSource:
#             if tag in data[1:]:
#                 #print(tag,data)
#                 temp_dict[data[0]] = temp_dict.get(data[0],0) + 1 

#     print(temp_dict)
#     for _ in range(len(temp_dict)): #temp_dict 만큼 반복
#         if len(temp_dict) == 0: #temp_dict 길이 0이면 중단
#             break

#         temp_max_val = max(temp_dict.values())
#         temp_list = sorted([key for key, val in temp_dict.items() if temp_max_val == val])
        
#         #최대값 해당되는 키 삭제
#         for key in temp_list:
#             del temp_dict[key]
#         answer += temp_list

#     print("연습", answer)
    

#     return answer

# dataSource =[
#     ["doc1", "t1", "t2", "t3"],
#     ["doc2", "t0", "t2", "t3"],
#     ["doc3", "t1", "t6", "t7"],
#     ["doc4", "t1", "t2", "t4"],
#     ["doc5", "t6", "t100", "t8"]
# ]
# tags =["t1", "t2", "t3"]

# print(solution(dataSource, tags))



# #4번 계좌 출력
# def solution(snapshots, transactions):
#     answer = []
#     snap_dict = {}
#     for val in snapshots:
#         snap_dict[val[0]] = [int(val[1]),0]
    

#     tran_cnt = 1
#     for log in transactions:
#         temp_id = int(log[0]) #로그아이디
#         temp_por = log[1] #행동
#         temp_account = log[2] #계좌
#         temp_money = int(log[3]) #돈
#         if snap_dict.get(temp_account):
#             if snap_dict[temp_account][1:].count(temp_id) == 0:
#                 snap_dict[temp_account].append(temp_id)
#                 if temp_por == 'SAVE':
#                     snap_dict[temp_account][0] += temp_money
#                 elif temp_por == 'WITHDRAW':
#                     snap_dict[temp_account][0] -= temp_money
#             else: #만약 로그아이디가 존재하면
#                 print("id가 이미 존재")
#                 continue
#         else: #계좌 존재 안하면
#             snap_dict[temp_account] = [temp_money,0]
#     print("스냅샷", snap_dict)
    
#     #정리
#     for i,j in snap_dict.items():
#         answer.append([i,str(j[0])])


#     return answer

# snapshots = [
#   ["ACCOUNT1", "100"], 
#   ["ACCOUNT2", "150"]
# ]
# transactions = [
#   ["1", "SAVE", "ACCOUNT2", "100"],
#   ["2", "WITHDRAW", "ACCOUNT1", "50"], 
#   ["1", "SAVE", "ACCOUNT2", "100"], 
#   ["4", "SAVE", "ACCOUNT3", "500"], 
#   ["3", "WITHDRAW", "ACCOUNT2", "30"]
# ]
# print(solution(snapshots,transactions))


# #2번 부정처리 찾기
# def solution(answer_sheet, sheets):
#     answer = -1
#     for num in answer_sheet:
#         print(num)


#     return answer

# answer_sheet =  "4132315142"
# sheets = ["3241523133","4121314445","3243523133","4433325251","2412313253"]
# print(solution(answer_sheet,sheets))


#의심 문항 = 같은 선택지를 골랐으나 오답인 문항
#부정행위 가능성 지수 = 총 의심 문항의 수 + (가장 긴 연속된 의심 문항의 수)2


# #1번 괄호쌍 찾기
# def solution(inputString):
#     answer = 0
#     string_1 = ['(','[','{','<']
#     string_2 = [')',']','}','>']
#     string_1_cnt = 0
#     string_2_cnt = 0
#     temp = []
#     for i in inputString:
#         if i in string_1: 
#             temp.append('(')
#             string_1_cnt += 1
#         elif i in string_2:
#             temp.append(')')
#             string_2_cnt += 1

#     print(temp)
#     len_temp = len(temp)
#     # 괄호 갯수 짝수 아닐경우 -1, 열괄,닫괄 개수 서로 안맞을 경우 -1
#     if len_temp % 2 != 0:
#         print("짝수가 아님")
#         return -1
#     if string_1_cnt != string_2_cnt:
#         return -1

#     print(string_1_cnt, string_2_cnt)

#     # 괄호 검증
#     bal_cnt = 0
#     i = 0
#     while 1:
#         if len(temp) == 0:
#             break

#         if i == 0 : #초기 설정
#             if temp[0] in string_1: 
#                 bal_cnt += 1
#                 temp.pop(0)
#             elif temp[0] in string_2:
#                 return -1
            
#         if i > 0 :
#             if temp[0] in string_1:# 열괄일때
#                 bal_cnt += 1
#             elif temp[0] in string_2:
#                 bal_cnt -= 1
#             temp.pop(0)

#             if bal_cnt == 0:
#                 answer += 1
#             if bal_cnt < 0:
#                 return -1
        
#         i += 1

#     return answer

# a = "if (Count of)) ()((eggs is 4.) Buy milk."
# print(solution(a))