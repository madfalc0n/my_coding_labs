def solution(info, query):
    user_dict = dict()
    for i,d in enumerate(info):
        user_dict[i] = d.split()

    result_list = []
    for q in query:
        cnt = 0
        tmp_q = q.replace("and",'').split()
        #print((tmp_q))
        for i,d in user_dict.items():
            #print(i,d)
            if tmp_q[0] == d[0] or tmp_q[0] == '-':
                if tmp_q[1] == d[1] or tmp_q[1] == '-':
                    if tmp_q[2] == d[2] or tmp_q[2] == '-':
                        if tmp_q[3] == d[3] or tmp_q[3] == '-':
                            if int(tmp_q[4]) <= int(d[4]):
                                cnt += 1
        result_list.append(cnt)

    return result_list


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))