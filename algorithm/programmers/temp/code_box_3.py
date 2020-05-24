"""
total_sp는 규칙에 맞게 정확히 분배할 수 있는 경우만 입력으로 주어집니다.
어떤 규칙?
"""

def solution(total_sp, skills):
    minimum_sp = int(total_sp**0.5) #최소 SP
    skill_dict = {}
    point_dict = {}
    skill_list = []
    answer = []

    #dict 정리
    for skill_info in skills:
        top_skill = skill_info[0] #상위스킬
        down_skill = skill_info[1] #하위스킬
        if down_skill not in skill_list:
            skill_list.append(down_skill)
            point_dict[down_skill] = minimum_sp #최상위 빼고 초기화
        skill_dict[top_skill] = skill_dict.get(top_skill,[]) + [down_skill]
    
    # print(f"skill_dict : {skill_dict}")
    # print(f"point_dict : {point_dict}") 
    # print(f"skill_list : {skill_list}") # 최상위 빼고

    #최상위 스킬 찾기
    result = list(skill_dict.keys() - point_dict.keys())
    skill_list.append(result[0])
    skill_list.sort()
    #print(result[0])

    #최상위 스킬 - > 상위 스킬 - > 하위 스킬로 분류하기
    #스킬탐색하고 계산
    while True:
        remove_key = 0 #하위스킬 발견시 해당 Key 값으로 변경
        for key,val in skill_dict.items(): 
            tmp_switch = 0
            tmp_sum_list = []
            for val2 in val:
                if val2 in skill_dict.keys(): #키에 있다면
                    tmp_switch = 1
                    break
                else:
                    tmp_sum_list.append(point_dict[val2])
            if tmp_switch == 0: #키가 없으면 하위스킬
                # print(key,val)
                # print(tmp_sum_list)
                remove_key = key
                point_dict[key] = sum(tmp_sum_list)
        if remove_key != 0 :
            del skill_dict[remove_key]
        
        # print(skill_dict)
        # print(point_dict)
        if len(skill_dict) == 0: #탐색 완료되면 종료
            break

    # print(skill_dict)
    # print(point_dict)    
    # print(skill_list)
    answer = [point_dict[val] for val in skill_list ]
    
    return answer

total_sp = 121
skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
print(solution(total_sp,skills))