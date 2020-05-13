"""
bfs
순서는 다음과 같다.
123
456
789
*0#

"""
#1,4,7 은 무조건 왼손
#7,8,9 는 무조건 오른속
# 2,5,8,0 은 가까운 손가락


def bfs(start,des):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    tmp_visit = [[0,0,0] for _ in range(4)]
    tmp_visit[start[0]][start[1]] = 1
    visit = [start]
    queue = [start]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx <= 3 and 0 <= ny and ny <= 2: #좌표안에 포함되고
                if tmp_visit[nx][ny] == 0 and [nx,ny] not in visit:
                    visit.append([nx,ny])
                    tmp_visit[nx][ny] = tmp_visit[x][y] + 1
                    queue.append([nx,ny])
    return tmp_visit[des[0]][des[1]]

def solution(numbers, hand):
    answer = ''
    l_list = [1,4,7,10] #왼손잡이
    l_point = [3,0]
    
    r_list = [3,6,9,11] #오른손잡이
    r_point = [3,2]
    
    m_list = [2,5,8,0] #중간
    #m_point = [0,0]

    for i in numbers:
        if i in l_list:
            answer += 'L'
            l_tmp_point = l_list.index(i)
            l_point = [l_tmp_point,0]

        elif i in r_list:
            answer += 'R'
            r_tmp_point = r_list.index(i)
            r_point = [r_tmp_point,2]

        else: #중간에 값이 있다면, 왼손과 오른손의 거리를 각각 구함
            m_tmp_point = m_list.index(i)
            m_point = [m_tmp_point,1]
            
            l_val = bfs(l_point,m_point)
            r_val = bfs(r_point,m_point)

            # print('mid')
            # print(i)
            # print(l_point,r_point)
            # print(l_val,r_val)

            if l_val == r_val:
                if hand == 'left':
                    answer += 'L'
                    l_point = m_point

                else:
                    answer += 'R'
                    r_point = m_point

            elif l_val < r_val:
                answer += 'L'
                l_point = m_point

            elif l_val > r_val:
                answer += 'R'
                r_point = m_point

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
print(solution(numbers,hand))