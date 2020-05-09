def solution(skill, skill_trees):
    skill_dict = {}
    for i,s in enumerate(skill):
        skill_dict[s] = i+1
    #print(skill_dict)

    c_skill_tree = []
    for skill_tree in skill_trees: #["BACDE", "CBADF", "AECB", "BDA"]
        tmp = ''
        for s in skill_tree:
            if skill.count(s): #카운트가 있다면
                tmp += s
        c_skill_tree.append(tmp)
    #print(c_skill_tree) 


    answer = []
    for part_skill in c_skill_tree: #['BCD', 'CBD', 'CB', 'BD']
        check = 0
        skill_set = [0] * (len(skill)+1) # 0번째 인덱스는 사용x,
        #print(skill_set)
        for one_skill in part_skill:
            #print(part_skill,one_skill)
            s_index = skill_dict.get(one_skill) # 인덱스
            skill_set[s_index] = 1
            #print(skill_set)
            if skill_set[1:s_index].count(0):
                #print("check")
                check = 1
                break
                #print(part_skill,one_skill)
        if check == 0:
            answer.append(part_skill)
    #print(answer)

    return len(answer)



skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))