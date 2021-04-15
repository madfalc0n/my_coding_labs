"""
삼각 달팽이
https://programmers.co.kr/learn/courses/30/lessons/68645
"""
import itertools as itr

def solution(n):
    answer = [[0]*i for i in range(1,n+1)]
    direction = 0 # 0:down, 1:right, 2:up
    cur_x, cur_y = 0,0
    cnt = 1
    for i in range(n,0,-1):
        # print(f"num {i}")
        for limit in range(i):
            # print(cur_x,cur_y)
            if direction == 0 :
                answer[cur_x][cur_y] = cnt
                if limit != i-1:
                    cur_x += 1
                else:
                    cur_y += 1
            
            elif direction == 1 :
                answer[cur_x][cur_y] = cnt
                if limit != i-1:
                    cur_y += 1
                else:
                    cur_x -= 1
                    cur_y -= 1

            elif direction == 2 :
                answer[cur_x][cur_y] = cnt            
                if limit != i-1:
                    cur_x -= 1
                    cur_y -= 1
                else:
                    cur_x += 1

            cnt += 1
        direction = (direction + 1) % 3  

    result = []
    for i in (answer):
        result.extend(i)
    
    return result


print(solution(5))