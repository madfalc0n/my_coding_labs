"""
단어 몇개를 뽑아 단어셋트를 만들어야 함
셋트 안에는 모든 소문자 알파벳 26개가 포함되어야 함
"""
for test_case in range(1,int(input())+1):
    voca_list = int(input())

    temp_list = []
    for _ in range(voca_list):
        temp_list.append(input())

    temp_set = {}
    for v in temp_list:
        for vv in v:
            temp_set[vv] = temp_set.get(vv,0) +1
    print(temp_set)
    print(sorted(temp_set))