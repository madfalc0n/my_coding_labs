#후보키
"""
그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 
이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 
정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 
다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.

유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.

최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 
즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.
유일성과 최소성이 만족되어야 한다.
"""
from itertools import combinations
def solution(relation):
    user = len(relation)
    db = {'num': [] , 'name': [] , 'major' : [], 'grade' : []}
    for data in relation:
        db['num'].append(data[0])
        db['name'].append(data[1])
        db['major'].append(data[2])
        db['grade'].append(data[3])
        #db[data[0]] =[data[1],data[2],data[3]] 
    
    c_key_list = []
    n_c_key_list = []
    for key,val in db.items():
        if len(set(val)) == user: #유저 개수와 같을 경우
            c_key_list.append(key)
        else:
            n_c_key_list.append(key)
    print(db)
    print(c_key_list)
    print(n_c_key_list)

    tmp_c_key_list = []
    for i in range(2,len(n_c_key_list)+1):
        combi_n_c_key_list = list(combinations(n_c_key_list,i))
        print(f'combi_n_c_key_list : {combi_n_c_key_list}')
        
        for j in range(user):
            tmp_list = set()    
            for jj in combi_n_c_key_list:
                tmp = ''
                for jjj in jj:        
                    tmp += db[jjj][j]
                tmp_list.add(tmp)
                #print(f"tmp : {tmp}")
                print(f"tmp_list : {tmp_list}")

            if len(tmp_list) == user: #후보키 될 자격이 있다
                print(f"후보키6개 tmp_list : {tmp_list}")
                tmp_c_key_list.append(jj)

    print("후보키리스트")
    print(c_key_list)
    print(tmp_c_key_list)

        



    return len(c_key_list)


relation = [["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]]
print(solution(relation))


#스킬테스트
# def solution(record):
#     answer = []
#     log_2 = []
#     db = {}
#     for log in record:
#         tmp = log.split(' ')
#         if tmp[0] == 'Enter' or tmp[0] == 'Change': #들어온 경우 db에 등록
#             db[tmp[1]] = tmp[2]
    
#         log_2.append([tmp[0],tmp[1]])

#         #print(tmp)
#     #print(db)
#     #print(log_2)
#     for log in log_2:
#         command = log[0]
#         user = log[1]
#         if command == 'Enter':
#             s = db[user] + "님이 들어왔습니다."
#             answer.append(s)
#         elif command == 'Leave':
#             s = db[user] + "님이 나갔습니다."
#             answer.append(s)
    
#     return answer

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record)) 