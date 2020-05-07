"""

"""
def save_dict():
    dict = {}
    first = 65 #대문자 A
    for i in range(1,27):
        dict[i] = chr(first)
        first += 1
    return dict

def solution(msg):
    answer = []
    
    #사전생성
    dict = save_dict()
    #print(dict)
    
    #사전리스트 생성
    dict_val_list = [0] + list(dict.values()) #[0]붙이는 이유는 실제 인덱스와 맞춰주기 위함
    #print(dict_val_list)

    #압축진행
    i = 0
    while i < len(msg):
        print(answer)
        for j in range(i+1,len(msg)+1):
            print(f"i : {i}, j : {j}")
            print(msg[i:j])
            if msg[i:j] in dict_val_list:
                pass
            else:#없으면 사전에 등록
                dict_val_list.append(msg[i:j])
                answer.append(dict_val_list.index(msg[i:j-1]))
                i = j -1
                break
        
            if j == len(msg):
                answer.append(dict_val_list.index(msg[i:j]))
                i = len(msg)
                break
    #print(dict_val_list)
    
    return answer





msg = "ABABABABABABABAB"
print(len(msg))
print(solution(msg))