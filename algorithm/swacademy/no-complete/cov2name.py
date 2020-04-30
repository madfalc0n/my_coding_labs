for index in range(1,int(input())+1):
    case_number = int(input())
    temp_list = list(input().replace('?','!').replace('!','.').split('.'))
    case_list = []
    for i in range(case_number):
        case_list.append(temp_list.pop(0))
        answer_cnt = 0
        wrong_cnt = 0
        for i in case_list:
            char_to_ord = ord(i)
            if char_to_ord > 64 and char_to_ord < 91:
                answer_cnt += 1




        print(case_list)