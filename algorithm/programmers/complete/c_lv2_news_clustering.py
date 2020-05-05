import math

def cov(str):#소문자로 변경
    tmp_str = ''
    for d in str:
        ord_v = ord(d)
        if 65 <= ord_v and ord_v <= 90:
            tmp_str += chr(ord(d)+32)
        else:
            tmp_str += d
    return tmp_str

def create_list(str):
    tmp_list = []
    for i in range(len(str)-1):
        #print(str[i])
        ord_str = ord(str[i])
        ord_str2 = ord(str[i+1])       
        if 97 <= ord_str and ord_str <= 122:
            if 97 <= ord_str2 and ord_str2 <= 122:
                tmp_list.append(str[i:i+2])
    return tmp_list


def solution(str1, str2):
    conv_str1 = cov(str1)
    conv_str2 = cov(str2)
    # print(conv_str1)
    # print(conv_str2)
    conv_list1 = create_list(conv_str1)
    conv_list2 = create_list(conv_str2)
    # print(conv_list1)
    # print(conv_list2)
    if len(conv_list1) == 0 and len(conv_list2) == 0 :
        return 65536
    
    tmp_list = [] #교집합 리스트 저장용
    tmp_cov_list1 = conv_list1.copy()
    tmp_cov_list2 = conv_list2.copy()
    
    #교집합 계산
    i = 0
    while True:
        #print(i)
        #print(tmp_cov_list1, tmp_cov_list2)
        
        if len(tmp_cov_list2) == 0 or len(tmp_cov_list1) == 0 or i == len(tmp_cov_list1):
                break
        if tmp_cov_list1[i] in tmp_cov_list2:
            #print(tmp_cov_list1[i])
            val = tmp_cov_list1.pop(i)
            val_index = tmp_cov_list2.index(val)
            tmp_list.append(tmp_cov_list2.pop(val_index))
            continue
        i += 1

    
    len_tmp_list = len(tmp_list)
    len_max_list = len(conv_list1) + len(conv_list2) - len(tmp_list)
    if len_tmp_list == 0: #교집합이 0일 경우
        answer = 0
    elif len_max_list == 0: #합지밥이 0일 경우
        answer = 65536
    elif len_tmp_list != 0 and len_tmp_list != 0:
        answer = math.trunc((len_tmp_list/len_max_list) * 65536)
    return answer   



str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1,str2))
