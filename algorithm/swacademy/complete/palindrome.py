"""
회문검사
하나의 문장을 거꾸로해도 똑같은 문장일 경우 회문이라고 함
회문일경우 1을 리턴 아닐경우 0을 리턴
"""
save_list = []
for i in range(1,int(input())+1):
    input_str = input()
    if input_str == input_str[::-1]:
        save_list.append(1)
    else:
        save_list.append(0)


for i,d in enumerate(save_list):
    print(f"#{i+1} {d}")