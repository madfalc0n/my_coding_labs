"""
숫자를 맞추는 야구게임
완전탐색, 주어진 조건을 통해 전체의 수와 비교
1~9 사이의 값으로 이루어진 3자리의 수를 찾는것
"""

from itertools import permutations

def cal_r(data,data2): #324 123
    # if data2 == 123:
    #     print(data,data2)
    data = list(map(str,data))
    data = ''.join(data)
    data2 = str(data2)


    #스트라이크, 볼 설정 
    s = 0 
    b = 0
    for i in range(3):
        if data[i] in data2: #값이 있는 경우
            if data2.index(data[i]) == i: #위치가 같은경우
                s += 1
            else:
                b += 1
    return [s,b] #스트라이크와 볼을 리스트 형식으로 반환



def solution(baseball):
    cnt = 0
    all_v = list(permutations(range(1,10),3)) #모든 수
    baseball_ball =list(map(lambda x:x[0], baseball)) #숫자만 추출
    print(baseball_ball)
    baseball_result = list(map(lambda x: [x[1],x[2]],baseball )) #결과만 추출
    print(baseball_result)

    
    for data in all_v:
        tmp_result_list = []
        for i in range(len(baseball_ball)):
            result = cal_r(data,baseball_ball[i])
            tmp_result_list.append(result)
        #print(data)
        #print(tmp_result_list)
        if tmp_result_list == baseball_result: #결과가 같다면 원하는 값
            #print(result)
            cnt += 1

    return cnt


baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	
print(solution(baseball))