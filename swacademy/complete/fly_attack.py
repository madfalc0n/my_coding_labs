"""
N * N 지역에 M*M 의 파리채로 파리 잡기

"""
def kill_sum(test_area, flapper, cur_x, cur_y):
    sum_cnt = 0
    #sum_cnt += sum([test_area[i][k] for i in range(cur_x, flapper + cur_x) for k in range(cur_y, flapper + cur_y)])
    sum_cnt += sum([ sum(test_area[i][cur_y:flapper + cur_y]) for i in range(cur_x, flapper + cur_x)])
    return sum_cnt


test_case = int(input())
for bi in range(test_case):
    area, flapper = map(int, input().split(" "))
    #print(test_case, area, flapper)
    test_area = []
    for _ in range(area):
        test_area.append(list(map(int,input().split(' '))))

    result = 0
    repeat_cnt = (area - flapper) + 1
    for x in range(repeat_cnt):
        for y in range(repeat_cnt):
            temp_sum_cnt = kill_sum(test_area, flapper, x,y)
            print(temp_sum_cnt)
            if temp_sum_cnt > result:
                result = temp_sum_cnt
    print(f"#{bi+1} {result}")


"""
유사코드
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arrs = []
    for _ in range(N):
        arrs.append(list(map(int, input().split())))
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = sum( sum(arrs[x][j:j + M]) for x in range(i, i + M))
            result = max(result, temp)
 
    print(f'#{T} {result}')
"""