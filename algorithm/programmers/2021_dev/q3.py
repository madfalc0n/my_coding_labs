
def solution(enroll, referral, seller, amount):
    user_dict = dict()
    money_dict = dict()
    amount = list(map(lambda x : x * 100 , amount))
    for i in range(len(enroll)):
        tmp_user = enroll[i]
        refer = referral[i]
        user_dict[tmp_user] = user_dict.get(tmp_user,[]) + [refer,0]
    

    for i in range(len(seller)):
        s_user = seller[i]
        s_amount_9 = int(amount[i] * 0.9)
        s_amount_1 = int(amount[i] * 0.1)
        user_dict[s_user][1] += s_amount_9
        next_user = user_dict[s_user][0]
        next_amount = s_amount_1
        print(f"first_user : {s_user} , cur_amount : {user_dict[s_user][1]}, next_amount : {next_amount}")
        while 1:
            if next_user == '-':
                break
            else:
                s_user = next_user
                next_user = user_dict[s_user][0]
                s_amount_9 = int(next_amount * 0.9)
                s_amount_1 = int(next_amount * 0.1)
                next_amount = s_amount_1
                user_dict[s_user][1] += s_amount_9
                print(f"cur_user : {s_user} , sum_amount : {s_amount_9}, next_amount : {next_amount}, cur_amount : {user_dict[s_user][1]}")
                
                

    print(user_dict)
    result = list(map(lambda x : x[1] , user_dict.values()))

    return result


e = ["john", "mary", "edward", "sam",    "emily", "jaimie", "tod", "young"]
r = ["-",     "-",     "mary", "edward", "mary",  "mary", "jaimie", "edward"]
s = ["young", "john", "tod", "emily", "mary"]
a = [12, 4, 2, 5, 10]

print(solution(e,r,s,a))