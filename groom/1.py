

h,u,d,f = map(int, input().split(' ')) # H,U,D,F
#user_input =  input()
#user_input = user_input.split(' ')

cu = 0 # 올라간거리
df = u * f * 0.001

i = 1 #소요일 수
while True:
    if i > 1:
        value = (i*u + ((i-1)*cu)) - ((i+2)*df) - ((i-1)*d)
    else:
        value = u+cu-df
    print(value)
    if value > h:
        print(f"Success {i}")
        break
    elif value < 0 :
        print(f"Failure {i}")
        break  
    i += 1
# while True:
#     #print(f"{i}번째 날")
#     if i != 1:
#         u -= df
#     #print(f"현재높이{cu}")
#     #print(f"피로도 {f}% 때문에 오늘은 {u} 만큼 올라갈 수 있다.")
#     #print(f"올라간 거리{u}")
#     # U높이만큼 올라간다
#     #print(f"{u}미터 만큼 올라갔다")
    
#     cu += u
#     #print(f"올라간 후 높이{cu}")
#     if cu > h:
#         print(f"Success {i}")
#         break

#     #print('밤이되었다')
#     #print(f'{d}만큼 내려왔다.')
#     cu -= d
#     #print(f"자는동안 내려간 후 높이{cu}")
#     if cu < 0:
#         print(f"Failure {i}")
#         break    
#     i +=1




#print(user_input)



