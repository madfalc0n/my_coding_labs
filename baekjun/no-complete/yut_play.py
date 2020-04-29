player = 4
player_place = [0] * player
yut_list = {
    0: [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
    10 : [13,16,19,25,30,35,40],
    20 : [22,24,25,30,35,40],
    30 : [28,27,26,25,30,35,40],
    40 : ['end']
}

def yut_p(player_list):#사용자의 위치와 점수를 반환
    point = 0
    place = 0
    current_place = -1 #시작점
    current_list = yut_list[0]
    for i,d in enumerate(player_list):
        current_place += d #실제 이동하는 위치
        point += current_list[current_place] #포인트를 누적
        if yut_list.get(current_list[current_place]) != None: #이동한 위치에 set key가 있다면 list 변경
            current_list = yut_list[current_list[current_place]]
            current_place = -1

    return point, current_place

for i in range(player):
    player_list = list(map(int,input().split(' ')))
    user_point, user_place = yut_p(player_list)
    print(user_point)
    player_place[i] = user_place