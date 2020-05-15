"""
4012 요리사
N개의 식재료가 있다.
식재료들을 각각 N / 2개씩 나누어 두 개의 요리를 하려고 한다. (N은 짝수이다.)
이때, 각각의 음식을 A음식, B음식이라고 하자.

비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 한다.
음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게 된다.

식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생한다. (1 ≤ i ≤ N, 1 ≤ j ≤ N, i ≠ j)
각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합이다.

식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어지고, 
가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 
두 음식 간의 맛의 차이가 최소가 되는 경우를 찾고 그 최솟값을 정답으로 출력하는 프로그램을 작성하라.
"""
from itertools import permutations, combinations

def bfs(matrix,point):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visit = [point]
    queue = [point]
    result = []
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx and nx <= len(matrix) and 0 < ny and ny <= len(matrix): #내부 영역 내에서 움직여야 함
                if nx != x and nx != y and ny != x and ny != y : #좌표가 현 위치와 일치하지 않아야 함
                    if [nx,ny] not in visit:
                        if nx != point[0] or nx != point[1] or ny != point[0] or ny != point[1]:
                            val1 = matrix[point[0]][point[1]] + matrix[point[1]][point[0]]
                            val2 = matrix[nx][ny] + matrix[ny][nx]
                            result.append(abs(val1-val2))
                            visit.append([nx,ny])


    return result



for i in range(1,int(input())+1):
    N = int(input())
    list_v = [ number for number in range(1,N+1)]
    combi_list = []
    combi_list = list(combinations(list_v,2))
    print(combi_list)
    

    # combi_result = []
    # tmp_i = 0
    # data = []
    # data2 = []
    # while tmp_i < len(combi_list):
    #     data = combi_list[tmp_i]
    #     for j in range(i+1,len(combi_list)):
    #         if combi_list[j][0] in data or combi_list[j][1] in data: # data에 값 포함될 경우
    #             continue
    #         else:
    #             data2 = combi_list[j]
    #             combi_result.append([data,data2])
    #     tmp_i += 1
    # print(combi_result)

    #matrix 초기화 및 입력값 받기
    matrix = [[0] * (N+1) for _ in range(N+1)]
    for n_v  in range(1,N+1):
        list_food_taste = list(input().split(' ') )
        list_food_taste = list(map(int,list_food_taste))
        matrix[n_v][1:] = list_food_taste
    
    for abc in matrix:
        print(abc)

    answer_list = []
    for point in combi_list:
        tmp_list = bfs(matrix,list(point))
        answer_list.extend(tmp_list)
    print(answer_list)

    # min_val = 20001
    # for data_list in combi_result: #((1, 2), (1, 3))
    #     #print(data_list[0], data_list[1])
    #     x = data_list[0][0]
    #     y = data_list[0][1]
    #     tmp_val_1 = matrix[x][y] + matrix[y][x]

    #     x = data_list[1][0]
    #     y = data_list[1][1]
    #     tmp_val_2 = matrix[x][y] + matrix[y][x]

    #     #print(tmp_val_1, tmp_val_2)
    #     result = abs(tmp_val_1 - tmp_val_2)
    #     #print(f"result : {result}") 
    #     if min_val > result:
    #         min_val = result

    print(f"#{i} {min_val}")