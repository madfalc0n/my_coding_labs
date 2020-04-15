input_num = int(input())

result_str = ""
for i in range(1,input_num+1):
    temp_str = str(i)
    temp_cnt = 0
    for val in temp_str:
        if val == '0':
            continue
        if int(val)%3 == 0:
            temp_cnt += 1
    if temp_cnt == 0:
        result_str += temp_str + " "
    else:
        result_str += '-' * temp_cnt + " "

print(result_str[:-1])