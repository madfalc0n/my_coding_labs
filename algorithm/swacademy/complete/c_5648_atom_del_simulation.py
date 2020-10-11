"""
원자 소멸 시뮬레이션
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRFInKex8DFAUo&categoryId=AWXRFInKex8DFAUo&categoryType=CODE
"""

def proc(atom_list, total_energy):
    #0 - 상, 1 - 하, 2 - 좌, 3 - 우
    dx = [0.0,0.0,-0.5,0.5]
    dy = [0.5,-0.5,0.0,0.0]
    for _ in range(4001):
        move_list = dict()
        remove_list = set()
        if len(atom_list) < 2:
            break
        
        #원자들 순환하면서 충돌하는 애들 있는지 판별, move_list에 좌표: 원자값 저장
        for i in range(len(atom_list)):
            #x,y 좌표 호출 및 방향에 따른 재갱신
            tmp_x, tmp_y = atom_list[i][0], atom_list[i][1]
            tmp_x += dx[atom_list[i][2]]
            tmp_y += dy[atom_list[i][2]]

            #범위 벗어나면 제거대상에 추가
            if  (-1000 > tmp_x  or tmp_x > 1000)  or (-1000 > tmp_y  or tmp_x > 1000):
                remove_list.add(i)
                continue
            atom_list[i][0] = tmp_x
            atom_list[i][1] = tmp_y
            tmp_str = (tmp_x, tmp_y)
            move_list[tmp_str] = move_list.get(tmp_str,[]) + [i]

        for key in move_list.keys():
            tmp_energy = 0
            if len(set(move_list[key])) > 1:
                for i in range(len(move_list[key])):
                    tmp_index = set(move_list[key])
                    tmp_energy = sum([atom_list[idx][3] for idx in tmp_index])
                    remove_list = remove_list | tmp_index
            total_energy += tmp_energy

        for idx in sorted(remove_list, reverse=True):
            atom_list.pop(idx)

    return total_energy


tc = int(input())
for case in range(1,tc+1):
    N = int(input())
    total_energy = 0
    atom_list = []
    for i in range(N):
        atom_list.append(list(map(int,input().split())))
    # print(atom_list)
    if len(atom_list) == 1:
        total_energy = 0
    else:
        total_energy = proc(atom_list,total_energy)
    print(f"#{case} {total_energy}")
        