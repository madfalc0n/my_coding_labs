"""
활주로 만들기
NxN의 N길이와 경사로 x 길이가 주어짐
1. 셀의 변화량을 찾기
2. 탐색은 1,1~N 까지 세로로 수행하고, 1~N,1 까지 가로로 수행
3. 변화량이 있는 기준으로 x 길이만큼 일정한 애들이 있는경우 활주로 만들수 있다고 판단
4. 변화량이 1인 애들을 먼저 찾는다(1보다 큰애들은 활주로 못만드는 놈들이므로 패스).


"""
def horizontal(matrix,start,runway_length): #세로로 탐색 
    x,y = start
    cur_stat = 0 #걸어온 길
    permission = False
    cur_val = matrix[x][y]
    while x < len(matrix)-1:
        x += 1
        cur_stat += 1
        if cur_stat >= runway_length: #요구하는경사로길이보다 클경우 경사로 설치가능
            permission = True  
        if (cur_val - matrix[x][y]) == 0: # 똑같으면 패스
            continue
        elif (cur_val - matrix[x][y]) == 1: # 이전보다 작을때
            #먼저 경사로 설치가능한지 확인
            if (x+runway_length)-1 <= len(matrix)-1:
                #가능한경우 길이까지 합 확인
                cur_val = matrix[x][y]
                tmp_sum = 0
                for cur_index in range(x,x+runway_length):
                    tmp_sum += matrix[cur_index][y]
                if cur_val*runway_length == tmp_sum: #같으면 설치가능
                    x = (x+runway_length)-1
                    permission = False
                    cur_stat = 0
                    continue
                else:
                    return 0
            else:
                return 0
        
        elif (cur_val - matrix[x][y]) == -1: # 이전보다 클때
            if permission: # 경사로 설치가능?
                cur_val = matrix[x][y]
                permission = False
                cur_stat = 0
                continue
            else:#경사로 설치불가능하면 활주로 못만듬
                return 0
        
        elif abs(cur_val - matrix[x][y]) > 1: # 변화량이 1보다 크면 활주로 못만듬
            return 0  
    print(start)
    return 1


def vertical(matrix,start,runway_length): # 가로로 탐색
    x,y = start
    cur_stat = 0 #걸어온 길
    permission = False
    cur_val = matrix[x][y]
    while y < len(matrix)-1:
        y += 1
        cur_stat += 1
        if cur_stat >= runway_length: #요구하는경사로길이보다 클경우 경사로 설치가능
            permission = True  
        if (cur_val - matrix[x][y]) == 0: # 똑같으면 패스
            continue
        elif (cur_val - matrix[x][y]) == 1: # 이전보다 작을때
            #먼저 경사로 설치가능한지 확인
            if (y+runway_length)-1 <= len(matrix)-1:
                #가능한경우 길이까지 합 확인
                cur_val = matrix[x][y]
                tmp_sum = 0
                for cur_index in range(y,y+runway_length):
                    tmp_sum += matrix[x][cur_index]
                if cur_val*runway_length == tmp_sum: #같으면 설치가능
                    y = (y+runway_length)-1
                    permission = False
                    cur_stat = 0
                    continue
                else:
                    return 0
            else:
                return 0
        
        elif (cur_val - matrix[x][y]) == -1: # 이전보다 클때
            if permission: # 경사로 설치가능?
                cur_val = matrix[x][y]
                permission = False
                cur_stat = 0
                continue
            else:#경사로 설치불가능하면 활주로 못만듬
                return 0
        
        elif abs(cur_val - matrix[x][y]) > 1: # 변화량이 1보다 크면 활주로 못만듬
            return 0  
    print(start)
    return 1


for index in range(1,int(input())+1):
    N,x = list(map(int,input().split(' ')))
    #print(N,x)
    matrix = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        heights_list = list(input().split(' ') )
        #print(heights_list)
        if heights_list[-1] == '':
            heights_list = list(map(int,heights_list[:-1]))
        else:
            heights_list = list(map(int,heights_list))
        matrix[i] = [0] + heights_list

    # for m in matrix:
    #     print(m)


    result = 0
    #가로 세로 축 탐색, x, y축 증가
    for point in range(1,N+1):
        re_1 = horizontal(matrix,[1,point],x) #세로축 기준으로 탐색
        re_2 = vertical(matrix,[point,1],x) #가로축 기준으로 탐색
        result += (re_1 + re_2)

    print(f"#{index} {result}")