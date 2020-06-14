# 장그래가 마부장과의 등산에서 최대한 빨리올라가기 위한 계획법?
"""
탈수방지를 위해 1키로당 1리터의 물을 마셔야 함
리스트는 각 키로별 약수터의 거리
리턴은 최대한 빨리 등산하기 위해 들린 약수터 리스트

"""
def select_stops(water_stops, capacity):
    result_list = []
    cur_point = 0
    last_point = water_stops[-1]
    cur_capacity = capacity
    for index in range(len(water_stops)-1):
        #print(f"cur water_stops : {water_stops[index]},  cur point : {cur_point}, cur capacity : {cur_capacity}")
        # 갈 수 있으면 뻐티기
        if cur_capacity+cur_point >= water_stops[index+1]:
            continue 
        # 갈 수 없으면 가까운 곳에서 채우기
        else:
            result_list.append(water_stops[index])
            cur_point = water_stops[index]
            cur_capacity = capacity
    result_list.append(last_point)

    return result_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))