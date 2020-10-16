from itertools import combinations
from copy import deepcopy
from _collections import deque


def check(lab_tmp):  # 오염 안된 구역이 있는지 없는지 확인
    for i in range(n):
        for j in range(n):
            if lab_tmp[i][j] == '0':
                return False
    else:
        return True


def infection(virus):
    global min_time
    tmp_lab = deepcopy(lab)
    virus = deque(virus)
    for i, j in virus:  # 처음 활성화 시킬 바이러스를 0으로 초기화 해주고
        tmp_lab[i][j] = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    time = 0
    virus_cnt = 0
    while virus:  # 바이러스를 퍼뜨리는 작업
        if virus_cnt == virus_count:  # 모든바이러스를 퍼뜨리면 break( 비활성화 된 바이러스는 굳이 활성화 시킬 필요 없다)
            break
        x, y = virus.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if tmp_lab[nx][ny] == '2':
                    virus.append((nx, ny))
                    tmp_lab[nx][ny] = tmp_lab[x][y] + 1
                    time = tmp_lab[nx][ny]

                elif tmp_lab[nx][ny] == '0':
                    virus.append((nx, ny))
                    tmp_lab[nx][ny] = tmp_lab[x][y] + 1
                    virus_cnt += 1  # 빈공간을 오염시켰을 때는 +1을 해준다.
                    time = tmp_lab[nx][ny]  # time에는 마지막 시간을 덮어씌워준다.

        if time > min_time:  # 가지치기 | 최솟값보다 크면 return
            return

    if check(tmp_lab):  # 모든 구역이 오염됐다면 break
        pass
    else:
        time = 2500

    min_time = min(time, min_time)


n, m = map(int, input().split())
lab = [input().split() for _ in range(n)]
min_time = 2500


virus_all = []  # 모든 바이러스의 위치를 저장
virus_count = 0  # 바이러스의 개수 -> 나중에 바이러스 퍼뜨릴 때 바이러스가 이미 다 퍼져있음에도 비활성화된 바이러스로 퍼져가려는 것을 막기 위해!
for i in range(n):
    for j in range(n):
        if lab[i][j] == '2':
            virus_all.append((i, j))
        elif lab[i][j] == '0':
            virus_count += 1

virus_combis = combinations(virus_all, m)  # 바이러스를 활성화 시킬 수 있는 갯수에 따른 경우의 수 만들기
for virus_combi in virus_combis:  # 각각의 경우의 수 마다 바이러스를 퍼뜨리는 함수 실행
    infection(virus_combi)

if min_time == 2500:  # 바이러스를 모두 퍼뜨릴 수 없는 경우
    print(-1)
else:  # 바이러스를 퍼뜨린 경우
    print(min_time)