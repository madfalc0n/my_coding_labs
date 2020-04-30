def solution(s):
    max_v = int(len(s) / 2)
    str_l = []
    str_l_len = []
    if len(s) < 2:
        return len(s)
    for i in range(1,max_v+1):
        #print(f"파트 {i}")
        temp = 0
        cnt = 1
        j = i
        sent = ''
        while True:
            print(f"{temp} , {temp + i} , {j}  ,{j + i} ")
            if s[temp:temp+i] == s[j:j+i]:
                cnt += 1
                j += i
            else: #틀리면 저장되어 있는 문장 저장하고 다음으로 넘어가야지
                if cnt != 1:
                    sent += str(cnt) + s[temp:temp+i]
                    temp = j
                    j += i
                else: #카운트가 1일 때 한칸씩 넘기도록
                    sent += s[temp:temp+i]
                    temp += i
                    j += i
                cnt = 1
                ##print(sent)

            if j >= len(s):
                #print("끝남")
                #print(f"{temp} , {i} ,{temp + i}  , {j}  ,{j + i} ")
                if cnt != 1:
                    sent += str(cnt) + s[temp:temp+i]
                else:
                    sent += s[temp:]
                str_l.append(sent)
                str_l_len.append((len(sent)))
                break
    print(str_l)
    print(str_l_len)
    return min(str_l_len)

#s = "aabbaccc"
#s = "abcabcdede"   
#s =  "abcabcabcabcdededededede"
#s = "xababcdcdababcdcd"
#s = "abcabcabcabcdededededede"
#s = 'aa' 
s = 'ababcdcdababcdcd'
print(solution(s))




# def solution(s):
#     max_v = int(len(s) / 2)
#     str_l = []
#     str_l_len = []
#     for i in range(1,max_v+1):
#         #print(f"파트 {i}")
#         temp = 0
#         cnt = 1
#         j = i
#         sent = ''
#         while True:
#             #print(f"{temp} , {temp + i} , {j}  ,{j + i} ")
#             if s[temp:temp+i] == s[j:j+i]:
#                 cnt += 1
#                 j += i
#             else: #틀리면 저장되어 있는 문장 저장하고 다음으로 넘어가야지
#                 if cnt != 1:
#                     sent += str(cnt) + s[temp:temp+i]
#                     temp = j
#                     j += i
#                 else: #카운트가 1일 때 한칸씩 넘기도록
#                     sent += s[temp]
#                     temp += 1
#                     j += 1
#                 cnt = 1
#                 ##print(sent)
#
#             if j+i > len(s):
#                 #print("끝남")
#                 #print(f"{temp} , {i} ,{temp + i}  , {j}  ,{j + i} ")
#                 if cnt != 1:
#                     sent += str(cnt) + s[temp:temp+i]
#                 else:
#                     sent += s[temp:]
#                 str_l.append(sent)
#                 str_l_len.append((len(sent)))
#                 break
#     print(str_l)
#     print(str_l_len)
#     return min(str_l_len)



# #s = "aabbaccc"
# #s = "abcabcdede"
# #s =  "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = "abcabcabcabcdededededede"
# print(solution(s))




# def solution(s):
#     answer = 0
#     #압축할 갯수 정해주는 코드
#     max_v = int(len(s)/2) # 최대 반복해서 확인할 갯수
#     #s = list(s)
#     str_l = []
#     str_l_len = []
#     sent = ''
#     for i in range(1,max_v+1):#1일때 하나씩 탐색, 2일 떄 2개씩 탐색...
#         cnt = 1
#         temp = 0
#         jump = 0
#         #for x in range(0,len(s),i): # 0 1 2 3 4 .,,,,, 0 2 4 6 8 .,,,,,,,0 3 6
#         for j in range(i,len(s)-i+1): # 전체-i 만큼 탐색 0 , 7
#             print(len(s))
#             if j+jump >= len(s):
#                 break
#             print(i, temp, j , jump)
#             #print(s[temp:temp+i]     ,   s[j:j+i])
#             if s[temp:temp+i] == s[j+jump:i+j+jump]: # 같을때
#                 print(s[temp:temp + i], s[j + jump:i + j + jump], "같고 : ", cnt)
#                 cnt +=1
#                 if j % 2 == 0 : # 짝수일떄
#                     if i%2 == 0 :
#                         jump += i-1
#                     else:
#                         jump += i-1
#                 else: # 홀 수 일때
#                     if i % 2 == 0:
#                         jump += i-1
#                     else:
#                         jump += i-1
#
#
#             else: #틀렸을 떄
#                 print(s[temp:temp + i], s[j+jump:i+j+jump], "틀렷고 : ", cnt)
#                 if cnt != 1:
#                     sent += (str(cnt)+s[temp:temp+i])
#                     temp = j+jump
#                     jump = 0
#                 else:
#                     sent += s[temp]#s[temp:temp+i]
#                     temp += 1
#                 cnt = 1
#         print("temp: ",cnt)
#         print("sent: ",sent)
#
#         if cnt != 1:
#             sent += (str(cnt)+s[temp:temp+i]) #s[j:j+i])
#         else:
#             sent += s[temp:j+i] #s[temp:temp+i]
#
#         print(sent)
#         str_l.append(sent)
#         str_l_len.append(len(sent))
#         sent = ''
#         print(str_l)
#
#     return str_l_len
#
#
# #s = "aabbaccc"
# #s = "abcabcdede"
# s =  "abcabcabcabcdededededede"
# print(solution(s))