words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    # 앞 뒤만 온다.
    db = save_db(words)
    q_result = matching(db, queries)
    f_result = fmatching(words,q_result)

    return f_result


def save_db(words):
    db = {}
    for i in range(len(words)):
        if db.get(len(words[i])):
            db[len(words[i])].append(words[i])
        else :
            db[len(words[i])] = [words[i]]
    ##print(db)
    return db

def matching(db, queries):
    db_2 = {}
    for i in range(len(queries)):
        q_len = len(queries[i]) # 단어 길이
        q_mark = queries[i].count('?') #물음표의 갯수
        if queries[i].startswith('?'): # ?로 시작하면
            db_2[queries[i]] = [q_len,'first' , q_mark ,queries[i][q_mark:] ]
            # if db_2.get(q_len):
            #     db_2[q_len].append(queries[i][q_mark:])

            # else :
            #     db_2[q_len] = [queries[i][q_mark:]]



        else: # 문자 시작하면 전체길이 - ? 길이 
            db_2[queries[i]] = [q_len ,'last' , q_mark ,queries[i][:q_len-q_mark]]
            # if db_2.get(q_len):
            #     db_2[q_len].append(queries[i][:q_len-q_mark])

            # else :
            #     db_2[q_len] = [queries[i][:q_len-q_mark]]
                  
    #print("Debug" ,db_2)
    return db_2


#["frodo", "front", "frost", "frozen", "frame", "kakao"]
def fmatching(words,q_result):
    #print("파이널 매칭")
    #print(words)
    #print(q_result)
    result_list = []
    for i in q_result.values():
        cnt = 0
        q_len = i[0]
        q_fl = i[1]
        q_mask = i[2]
        q_str = i[3]
        #print(q_len, q_fl, q_mask, q_str)
        if q_len == q_mask:
            cnt += 1
            continue
        for j in words:
            if q_len == len(j):
                if q_fl == 'first':
                    #print(j[q_mask:] , q_str)
                    if j[q_mask:] == q_str:
                        #print(j)
                        cnt += 1
                else:
                    #print(j[:q_len-q_mask] , q_str)
                    if j[:q_len-q_mask] == q_str:
                        #print(j)
                        cnt += 1
                
        result_list.append(cnt)
        cnt = 0
    return result_list




print(solution(words, queries))

##print(a.values())